library(data.table)
Source <- "/private/tmp/claude-501/-Users-averrik-Cloud-github-projects-AR-M2V4D/bc6bc387-e4e1-4ab5-a8cb-3e5e18735788/scratchpad/pdf2md-crawford-final-20261015/out/CAPR003324_Crawford_SeismicHazard_Final.md"
Lines <- readLines(Source, warn = FALSE)
Sections <- list(mean = 1171:1192, "0.84" = 1194:1214)
Diana <- rbindlist(lapply(names(Sections), function(p) {
  AUX <- Lines[Sections[[p]]]
  AUX <- gsub("*", "", AUX, fixed = TRUE)
  AUX <- AUX[grepl("^\\| [0-9]", AUX)]
  AUX <- lapply(strsplit(AUX, "|", fixed = TRUE), function(x) trimws(x[2:7]))
  DT <- as.data.table(do.call(rbind, AUX))
  setnames(DT, c("TR.diana", "1500", "910", "760", "580", "220"))
  DT[, names(DT) := lapply(.SD, function(x) as.numeric(gsub(",", "", x, fixed = TRUE)))]
  DT <- melt(DT, id.vars = "TR.diana", variable.name = "Vs30", value.name = "Diana")
  DT[, `:=`(Vs30 = as.numeric(as.character(Vs30)), p = p)]
  DT
}), use.names = TRUE)
stopifnot(nrow(Diana) == 50L, !anyNA(Diana), !anyDuplicated(Diana, by = c("TR.diana", "Vs30", "p")))
Correspondence <- data.table(TR.diana = c(475, 2475, 5000, 10000), TR = c(500, 2500, 5000, 10000))
Diana <- Correspondence[Diana[Vs30 %in% c(760, 1500) & TR.diana %in% Correspondence$TR.diana], on = "TR.diana"]
UHS <- readRDS("data/hazard/tables/UHSTable.Rds")
Report <- UHS[ID == "M2V4D" & siteID == "CFD" & Tn == 0 & Vs30 %in% c(760, 1500) & TR %in% Correspondence$TR & p %in% c("mean", "0.84"), .(TR, Vs30, p, Report = SaF)]
stopifnot(nrow(Report) == 16L, !anyNA(Report), !anyDuplicated(Report, by = c("TR", "Vs30", "p")))
Comparison <- Report[Diana, on = .(TR, Vs30, p)]
Comparison[, `:=`(difference = Report - Diana, percent = 100 * (Report / Diana - 1))]
stopifnot(nrow(Comparison) == 16L, !anyNA(Comparison))
setorder(Comparison, p, Vs30, TR)
fwrite(Comparison, "dev/SoT/m65-20261014/diana-sources/hazard-sanity.csv")
print(Comparison)
