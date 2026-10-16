library(data.table)

readDianaCurves <- function(root, vs30) {
  Spec <- jsonlite::fromJSON(file.path(root, "specs/calcs/classical/M2V4D.json"))
  Site <- jsonlite::fromJSON(file.path(root, "specs/sites/CFD.json"))
  rbindlist(lapply(vs30, function(v) {
    Archive <- file.path(root, "data/hazard/output/classical/M2V4D/CFD", v,
                         paste0("hazard_curves.M2V4D.CFD.", v, ".zip"))
    Members <- utils::unzip(Archive, list = TRUE)
    stopifnot(all(grepl("^(hazard|quantile)_curve-", Members$Name)), all(Members$Length < 10000))
    rbindlist(lapply(Members$Name, function(path) {
      Connection <- unz(Archive, path, open = "r")
      on.exit(close(Connection), add = TRUE)
      Lines <- readLines(Connection, warn = FALSE)
      stopifnot(length(Lines) == 3)
      Te <- as.numeric(sub(".*investigation_time=([0-9.]+).*", "\\1", Lines[[1]]))
      stopifnot(identical(Te, Spec$job$calculation$investigation_time))
      DT <- fread(text = paste(Lines[-1], collapse = "\n"), colClasses = "numeric")
      stopifnot(nrow(DT) == 1, DT$lon == round(Site$lon, 4), DT$lat == round(Site$lat, 4))
      Columns <- grep("^poe-", names(DT), value = TRUE)
      stopifnot(length(Columns) == Spec$imtl$n)
      IMT <- sub(".*-(PGA|SA\\([0-9.]+\\))_[0-9]+\\.csv$", "\\1", path)
      Period <- 0
      if (IMT != "PGA") Period <- as.numeric(sub("SA\\(([0-9.]+)\\)", "\\1", IMT))
      Stat <- sub("^(hazard|quantile)_curve-([^-]+)-.*", "\\2", path)
      POE <- as.numeric(DT[, ..Columns])
      stopifnot(!anyNA(POE), all(POE >= 0 & POE <= 1), is.finite(Period))
      data.table(Vs30 = v, Tn = Period, p = Stat,
                 Sa = as.numeric(sub("^poe-", "", Columns)), POE = POE,
                 AEP = -log1p(-POE) / Te, Te = Te, member = path)
    }))
  }))
}

readDiana <- function(root) {
  Layout <- jsonlite::fromJSON(file.path(root, "_local/hazard.diana.json"), simplifyVector = FALSE)
  UHS <- readRDS(file.path(root, "data/hazard/tables/UHSTable.Rds"))[
    ID == "M2V4D" & siteID == "CFD" & Vs30 %in% unlist(Layout$vs30)]
  UHS[p != "mean", p := as.character(as.numeric(p))]
  Keys <- c("Vs30", "TR", "Tn", "p")
  stopifnot(!anyDuplicated(UHS, by = Keys), all(is.finite(UHS$SaF)), all(UHS$SaF > 0))
  stopifnot(setequal(unique(UHS$Vs30), unlist(Layout$vs30)))
  Periods <- sort(unique(UHS$Tn))
  stopifnot(nrow(UHS) == length(Layout$vs30) * uniqueN(UHS$TR) * length(Periods) * uniqueN(UHS$p))
  NRC <- jsonlite::fromJSON(file.path(root, "dev/SoT/m65-20261014/diana-hazard/nrc2020-response.json"))
  stopifnot(is.null(NRC$errors))
  NRC <- rbindlist(NRC$data$NBC2020[setdiff(names(NRC$data$NBC2020), "metadata")])
  NRC[, Vs30 := vapply(vs30, function(x) x[[1]], numeric(1))]
  NRC[, TR := c(2500, 1000, 500)[match(poe50, c(2, 5, 10))]]
  NRC <- melt(NRC, id.vars = c("Vs30", "TR", "poe50", "foe"),
              measure.vars = c("pga", "sa0p05", "sa0p1", "sa0p2", "sa0p3", "sa0p5", "sa1p0", "sa2p0", "sa5p0", "sa10p0"),
              variable.name = "imt", value.name = "SaF")
  NRC[, Tn := c(0, 0.05, 0.1, 0.2, 0.3, 0.5, 1, 2, 5, 10)[match(imt, c("pga", "sa0p05", "sa0p1", "sa0p2", "sa0p3", "sa0p5", "sa1p0", "sa2p0", "sa5p0", "sa10p0"))]]
  stopifnot(!anyNA(NRC[, .(Vs30, TR, Tn, SaF)]), !anyDuplicated(NRC, by = c("Vs30", "TR", "Tn")))
  RMw <- readRDS(file.path(root, "data/hazard/tables/RMwTable.Rds"))[
    ID == "M2V4D" & siteID == "CFD" & Tn == 0 & TR %in% unlist(Layout$tr)]
  AEP <- readDianaCurves(root, unlist(Layout$vs30))
  stopifnot(!anyDuplicated(AEP, by = c("Vs30", "Tn", "p", "Sa")))
  list(layout = Layout, uhs = UHS, nrc = NRC, rmw = RMw, periods = Periods, aep = AEP)
}

dianaTable <- function(data, item) {
  DT <- data$uhs[p == item$stat & TR %in% unlist(data$layout$tr)]
  if (item$kind == "pga") {
    DT <- DT[Tn == 0, .(Row = TR, Vs30, SaF)]
    DT <- dcast(DT, Row ~ Vs30, value.var = "SaF")
    DT[, Row := unlist(data$layout$trLabel)[match(Row, unlist(data$layout$tr))]]
    DT[, (as.character(unlist(data$layout$vs30))) := lapply(.SD, function(x) formatC(x, format = "f", digits = 4)), .SDcols = as.character(unlist(data$layout$vs30))]
  }
  if (item$kind == "spectra") {
    DT <- DT[TR == item$tr, .(Row = Tn, Vs30, SaF)]
    DT <- dcast(DT, Row ~ Vs30, value.var = "SaF")
    DT[, Row := formatC(Row, format = "f", digits = 3)]
    DT[, (as.character(unlist(data$layout$vs30))) := lapply(.SD, function(x) formatC(x, format = "f", digits = 3)), .SDcols = as.character(unlist(data$layout$vs30))]
  }
  stopifnot(item$kind %in% c("pga", "spectra"), !anyNA(DT))
  setcolorder(DT, c("Row", as.character(unlist(data$layout$vs30))))
  DT
}

dianaPlot <- function(data, item) {
  if (item$kind == "rmw") {
    DT <- dcast(data$rmw[TR == item$tr], Mw ~ R, value.var = "p")
    Z <- as.matrix(DT[, -"Mw"])
    Graphics <- par(mar = c(1.5, 1.5, 2.5, 1.5))
    on.exit(par(Graphics), add = TRUE)
    persp(x = DT$Mw, y = as.numeric(names(DT)[-1]), z = Z * 100,
          theta = 35, phi = 25, expand = 1.2, col = "#2c7fb8", shade = 0.4,
          border = "#2b4b65", xlab = "Mw", ylab = "",
          zlab = "Contribution (%)", ticktype = "detailed", nticks = 4,
          main = paste0("PGA | TR = ", format(item$tr, big.mark = ","), " years"),
          cex.main = 0.75, cex.axis = 0.55, cex.lab = 0.65)
    mtext("Distance R (km)", side = 1, line = -1.3, adj = 0.95, cex = 0.65)
    return(invisible(NULL))
  }
  DT <- data$uhs[p == item$stat]
  if (item$kind %in% c("uhs", "nrc")) {
    DT <- DT[Vs30 == item$vs30 & TR %in% unlist(data$layout$tr)]
    if (item$kind == "nrc") DT <- DT[TR %in% c(500,1000,2500)]
    DT[, Series := factor(TR, levels = unlist(data$layout$tr))]
    PLOT <- ggplot2::ggplot(DT, ggplot2::aes(x = Tn, y = SaF, colour = Series)) +
      ggplot2::geom_line(linewidth = 0.55) +
      ggplot2::labs(x = "Spectral period (s)", y = "Spectral acceleration (g)", colour = "Return period (years)", subtitle = "5% damping")
    if (item$kind == "nrc") {
      NRC <- data$nrc[Vs30 == item$vs30 & Tn %in% data$periods]
      NRC[, Series := factor(TR, levels = unlist(data$layout$tr))]
      PLOT <- PLOT + ggplot2::geom_point(data = NRC, shape = 0, size = 2.1, stroke = 0.6) +
        ggplot2::labs(subtitle = "5% damping | Lines: project model | Squares: NRC 2020")
    }
  }
  if (item$kind == "design") {
    DT <- DT[TR == item$tr]
    DT[, Series := factor(Vs30, levels = unlist(data$layout$vs30))]
    PLOT <- ggplot2::ggplot(DT, ggplot2::aes(x = Tn, y = SaF, colour = Series)) +
      ggplot2::geom_line(linewidth = 0.55) +
      ggplot2::labs(x = "Spectral period (s)", y = "Spectral acceleration (g)", colour = "Vs30 (m/s)", subtitle = "5% damping")
  }
  if (item$kind == "aep") {
    DT <- data$aep[Vs30 == item$vs30 & p == item$stat & Tn %in% unlist(data$layout$aepPeriods) & is.finite(AEP) & AEP > 0]
    stopifnot(uniqueN(DT$Tn) == length(data$layout$aepPeriods))
    DT[, Series := factor(Tn, levels = unlist(data$layout$aepPeriods))]
    PLOT <- ggplot2::ggplot(DT, ggplot2::aes(x = Sa, y = AEP, colour = Series)) +
      ggplot2::geom_hline(yintercept = 1 / unlist(data$layout$tr), colour = "grey70", linetype = "dashed", linewidth = 0.25) +
      ggplot2::geom_line(linewidth = 0.55) +
      ggplot2::scale_x_log10() +
      ggplot2::scale_y_log10(sec.axis = ggplot2::sec_axis(~ 1 / ., name = "Return period (years)", breaks = unlist(data$layout$tr))) +
      ggplot2::coord_cartesian(xlim = c(0.001,10), ylim = c(1e-6,1)) +
      ggplot2::labs(x = "Spectral acceleration (g)", y = "Annual exceedance rate (1/year)",
                    colour = "Period (s)", subtitle = "Direct OpenQuake calculation")
  }
  stopifnot(item$kind %in% c("uhs", "nrc", "design", "aep"))
  PLOT + ggplot2::theme_bw(base_size = 10) +
    ggplot2::theme(legend.position = "bottom", legend.key.width = grid::unit(1.1, "cm"),
                   panel.grid.minor = ggplot2::element_blank(),
                   plot.margin = ggplot2::margin(5,8,5,5)) +
    ggplot2::guides(colour = ggplot2::guide_legend(nrow = if (item$kind == "aep") 2 else 1)) +
    ggplot2::scale_colour_manual(values = setNames(grDevices::hcl.colors(nlevels(DT$Series), palette = "Dark 3"), levels(DT$Series)))
}

dianaValues <- function(data, root) {
  Engine <- readLines(file.path(root, "dev/SoT/m65-20261014/diana-hazard/submit.log"))
  Engine <- sub(".* Engine: ", "", Engine[grepl("Engine:", Engine, fixed = TRUE)])
  stopifnot(length(Engine) == 1)
  Joint <- data$rmw[, .SD[which.max(p)], by = TR]
  Marginal <- data$rmw[, .(p = sum(p)), by = .(TR, Mw)][, .SD[which.max(p)], by = TR]
  Comparison <- merge(data$uhs[p == "mean" & Vs30 %in% c(1500,760,220)],
                      data$nrc[Tn %in% data$periods & Vs30 %in% c(1500,760,220)],
                      by = c("Vs30", "TR", "Tn"), suffixes = c(".project", ".nrc"))
  stopifnot(nrow(Comparison) == 3 * 3 * sum(unique(data$nrc$Tn) %in% data$periods))
  List <- list(engine = Engine, vref = unique(data$uhs$Vref),
               ratioMin = formatC(min(Comparison$SaF.project / Comparison$SaF.nrc), digits = 2, format = "f"),
               ratioMax = formatC(max(Comparison$SaF.project / Comparison$SaF.nrc), digits = 2, format = "f"),
               jointMw = range(Joint$Mw), jointR = range(Joint$R), marginalMw = range(Marginal$Mw),
               nrcPeriods = sort(unique(data$nrc[Tn > 0]$Tn)))
  for (t in c(2500,10000)) {
    for (Stat in c("mean", "0.84")) {
      x <- data$uhs[Vs30 == 220 & TR == t & Tn == 0 & p == Stat, SaF]
      stopifnot(length(x) == 1)
      List[[paste(t,Stat,sep = ".")]] <- formatC(x, digits = 3, format = "f")
    }
  }
  List
}
