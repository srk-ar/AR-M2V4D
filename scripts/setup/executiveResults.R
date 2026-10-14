# nolint start
# executiveResults.R: cross-site aggregates for the executive summary.
#
# Every per-site summary script keeps its single-site contract. This script
# runs them once per declared report site, each site in its own environment,
# and retains what the executive prose states across sites: the ranges of the
# values that vary by site, plus the site-independent dynamic properties.
# Values keep the producer units (accelerations in g, periods in s); the
# prose converts them where it needs other units.
# Expects the setup tables, SiteTable and root.

# One text for a range whose ends may coincide: "a" or "a<sep>b". The caller
# supplies the connector in its language and the formatter of the values.
.executiveRange <- function(x, sep, format) {
  TEXT <- format(range(as.numeric(x)))
  if (identical(TEXT[[1L]], TEXT[[2L]])) return(TEXT[[1L]])
  paste(TEXT, collapse = sep)
}

# Visible name of a tectonic region code: its declared entry, or the code
# itself when the project uses a code without a declared name (SIS30, SIS55).
.executiveRegime <- function(code, regime) {
  vapply(code, function(k) if (k %in% names(regime)) regime[[k]] else k, character(1), USE.NAMES = FALSE)
}

# Visible label of the acceleration units that the callers select through
# PSA_Units; the identifier stays as the conversion key.
.executiveUnits <- function(units) {
  LABEL <- c(g = "g", "cm/s2" = "$\\mathrm{cm/s^2}$")
  if (!units %in% names(LABEL)) {
    stop("executive summary: no label for units ", units, call. = FALSE)
  }
  LABEL[[units]]
}

# Citation of the adopted seismic source model, as its SSM chapter cites it.
SSM.CITATION <- c(
  SAM = "[@GEMHazardTeamSAM]",
  ARB = "[@GEMHazardTeamARB]",
  AUS = "[@AllenEtAl2023NSHA23; @AllenEtAl2024NSHA23Data]"
)

.executiveOne <- function(x, what) {
  VALUES <- unique(x)
  if (length(VALUES) != 1L) {
    stop("executive summary: ", what, " differs between the report sites.", call. = FALSE)
  }
  VALUES
}

ExecutiveSummary <- local({
  SCRIPTS <- c(
    "hazard.R", "dsha.R", "siteResults.R", "criteriaResults.R",
    "structures.R"
  )
  Sites <- lapply(SiteTable$siteID, function(site) {
    ENV <- new.env(parent = environment())
    ENV$siteID.target <- site
    ENV$PSA_Units <- "g"
    for (SCRIPT in SCRIPTS) {
      sys.source(file.path(root, "scripts", "setup", SCRIPT), envir = ENV)
    }
    ENV
  })
  names(Sites) <- SiteTable$siteID
  bySite <- function(extract) {
    data.table::rbindlist(lapply(names(Sites), function(site) {
      DT <- extract(Sites[[site]])
      if (is.null(DT)) return(NULL)
      data.table::data.table(siteID = site, DT)
    }), use.names = TRUE)
  }

  Rock <- bySite(function(ENV) ENV$PGA[Vs30 == 760 & p == "mean", .(TR, SaF)])
  Rock <- Rock[, .(minimum = min(SaF), maximum = max(SaF)), by = TR][order(TR)]

  Scenarios <- NULL
  Envelope <- NULL
  Governor <- NULL
  if (!is.null(Sites[[1L]]$DSHA.scn)) {
    DT <- bySite(function(ENV) ENV$DSHA.scn[, .(ID, TRT, Mw, Repi, PGA.mean)])
    # A scenario ID may be defined per site: its tectonic regimes and magnitudes
    # are kept as the set and the range across the report sites.
    Scenarios <- DT[, .(
      TRT = paste(sort(unique(TRT)), collapse = ","),
      Mw.minimum = min(Mw), Mw.maximum = max(Mw),
      Repi.minimum = min(Repi), Repi.maximum = max(Repi),
      PGA.minimum = min(PGA.mean), PGA.maximum = max(PGA.mean)
    ), by = ID][order(ID)]
    Envelope <- bySite(function(ENV) ENV$DSHA.mce)
    AUX <- MCETable[
      Tn == 0 & Vs30 == 760 & siteID %in% names(Sites) & ID == "MCE" & .matchP(p, "0.84"),
      .(siteID, PGA.p84 = SaF)
    ]
    if (nrow(AUX) && (nrow(AUX) != length(Sites) || anyNA(AUX$PGA.p84))) {
      stop("executive summary: the MCE (84%) PGA on reference rock is not unique per site.", call. = FALSE)
    }
    Envelope <- if (nrow(AUX)) merge(Envelope, AUX, by = "siteID") else Envelope[, PGA.p84 := NA_real_]
    Envelope <- Envelope[, .(
      minimum = min(PGA.mean), maximum = max(PGA.mean),
      minimum84 = min(PGA.p84), maximum84 = max(PGA.p84)
    )]
    Governor <- bySite(function(ENV) data.table::data.table(ID = ENV$DSHA.gov.mean))
  }

  # Mean and 0.84 quantile of the PGA on reference rock, per site, for the MDE
  # (probabilistic, TR.MDE) and the MCE envelope; NA where a statistic is absent.
  Statistics <- data.table::rbindlist(lapply(SiteTable$siteID, function(site) {
    pick <- function(DT, P) {
      DT <- DT[.matchP(p, P)]
      if (!nrow(DT)) return(NA_real_)
      DT <- DT[Tn == min(Tn)]
      if (nrow(DT) != 1L) return(NA_real_)
      DT$SaF
    }
    MDE <- UHSTable[siteID == site & ID %in% ID.gmdp & TR == TR.MDE & Vs30 == 760, .(p, Tn, SaF)]
    MCE <- if (!is.null(MCETable) && nrow(MCETable)) MCETable[siteID == site & ID == "MCE" & Vs30 == 760, .(p, Tn, SaF)] else MDE[0L]
    data.table::data.table(
      siteID = site, MDE.mean = pick(MDE, "mean"), MDE.p84 = pick(MDE, "0.84"),
      MCE.mean = pick(MCE, "mean"), MCE.p84 = pick(MCE, "0.84")
    )
  }))

  Demand <- bySite(function(ENV) ENV$SiteSummary$pgaMDE)
  Peak <- unique(Demand[, .SD[which.max(SaF)], by = siteID]$Vs30)
  PeakCondition <- if (length(Peak) == 1L) Peak else NA_real_

  .executiveOne(
    vapply(Sites, function(ENV) paste(ENV$CriteriaSummary$standards, collapse = ","), character(1)),
    "the set of design standards"
  )
  Bands <- bySite(function(ENV) ENV$CriteriaSummary$bands)
  Bands <- Bands[, .(minimum = min(PGA.min), maximum = max(PGA.max)), by = band][order(band)]

  Structures <- bySite(function(ENV) ENV$StructuresSummary$parameters[, .(Vs30, SDS, SD1)])

  sys.source(file.path(root, "scripts", "setup", "dynamics.R"), envir = environment())

  list(
    sites = SiteTable$siteID,
    ssm = list(
      label = Hazard.config$ssmLabel,
      citation = if (Hazard.config$ssmLabel %in% names(SSM.CITATION)) SSM.CITATION[[Hazard.config$ssmLabel]] else ""
    ),
    rock = Rock,
    scenarios = Scenarios,
    envelope = Envelope,
    governor = Governor,
    demand = Demand,
    statistics = Statistics,
    peakCondition = PeakCondition,
    criteria = list(standards = Sites[[1L]]$CriteriaSummary$standards, bands = Bands),
    structures = Structures,
    dynamics = DynamicsSummary
  )
})
# nolint end
