# nolint start
if (!exists("SSM_MODEL", inherits = FALSE) || !identical(SSM_MODEL, "AUS")) {
  stop("SSM.AUS.R: SSM_MODEL must be 'AUS'.", call. = FALSE)
}
if (!exists("SSM_FILE", inherits = FALSE) || length(SSM_FILE) != 1L) {
  stop("SSM.AUS.R: set SSM_FILE to SSMTable.Rds under the hazard contract path.data.", call. = FALSE)
}
if (!file.exists(SSM_FILE)) {
  stop(sprintf("SSM.AUS.R: required inventory not found: %s.", SSM_FILE), call. = FALSE)
}

DATA <- readRDS(SSM_FILE)
Schema <- c(
  "ID", "siteID", "providerID", "sourceName", "sourceType", "trt",
  "mfdType", "aValue", "bValue", "minMag", "maxMag",
  "mmaxLTType", "mmaxLTValues", "mmaxLTWeights",
  "abLTType", "abLTValues", "abLTWeights",
  "usd", "lsd", "hypoDepths", "meanHypoDepth", "midSeismoDepth",
  "dip", "rake", "traceLength", "seismoThickness", "downDipWidth",
  "magScaleRel", "ruptAspectRatio", "totalRate", "nMagBins",
  "lonMin", "lonMax", "latMin", "latMax", "hostKind", "Rjb", "Rrup",
  "distMethod", "nModelBranches", "branchVaries", "file"
)
Classes <- stats::setNames(rep("character", length(Schema)), Schema)
Classes[c("Rjb", "Rrup")] <- "numeric"
Classes[c("nModelBranches", "branchVaries")] <- "integer"

if (!inherits(DATA, "data.frame") || !identical(names(DATA), Schema)) {
  stop("SSM.AUS.R: SSMTable.Rds has an incompatible schema.", call. = FALSE)
}
if (!identical(vapply(DATA, class, character(1L)), Classes)) {
  stop("SSM.AUS.R: SSMTable.Rds has incompatible column types.", call. = FALSE)
}
DT <- data.table::as.data.table(DATA)
IdentityCols <- c("ID", "siteID", "providerID")
if (!nrow(DT) ||
    DT[, any(vapply(
      .SD,
      function(x) any(is.na(x) | !nzchar(trimws(x))),
      logical(1L)
    )), .SDcols = IdentityCols] ||
    data.table::uniqueN(DT$ID) != 1L ||
    data.table::uniqueN(DT$siteID) < 1L) {
  stop("SSM.AUS.R: inventory must contain one model ID and at least one site.", call. = FALSE)
}
NormalizedProvider <- sub(
  "[:;].*$", "", sub("!.*$", "", trimws(DT$providerID))
)
if (any(DT$providerID != NormalizedProvider)) {
  stop("SSM.AUS.R: providerID is not normalized as declared.", call. = FALSE)
}
SiteCount <- data.table::uniqueN(DT$siteID)
source(file.path(root, "scripts", "tbl", "ssmProvenance.R"), local = TRUE)
.validateSSMProvenance(DT, file = SSM_FILE, model = SSM_MODEL)
if (DT[, anyDuplicated(.SD), .SDcols = c("ID", "siteID", "providerID")]) {
  stop("SSM.AUS.R: inventory source identity is invalid.", call. = FALSE)
}
AUX <- DT[, .N, by = providerID]
if (any(AUX$N != SiteCount)) {
  stop("SSM.AUS.R: every AUS source must be represented at every declared site.", call. = FALSE)
}

IntrinsicCols <- setdiff(
  names(DT), c("siteID", "hostKind", "Rjb", "Rrup", "distMethod")
)
DT <- unique(DT[, ..IntrinsicCols])
if (anyDuplicated(DT$providerID)) {
  stop("SSM.AUS.R: source properties differ between project sites.", call. = FALSE)
}
if (DT[, any(is.na(mfdType) | mfdType != "EvenlyDiscretizedMFD")]) {
  stop("SSM.AUS.R: AUS recurrence is not the approved collapsed incremental model.", call. = FALSE)
}

DT[, TRT := vapply(
  strsplit(trt, "|", fixed = TRUE),
  function(x) paste(sort(unique(x)), collapse = "/"),
  character(1L)
)]
Observed <- DT[, .N, by = .(TRT, sourceType)]
Expected <- data.table::data.table(
  TRT = c("ASC", "ASC", "ASC", "ASC/SCC", "ASC/SCC", "SCC", "SCC", "SCC", "SIF", "SIS"),
  sourceType = c(
    "AreaSource", "PointSource", "SimpleFaultSource", "AreaSource",
    "PointSource", "AreaSource", "PointSource", "SimpleFaultSource",
    "ComplexFaultSource", "AreaSource"
  ),
  N = c(226L, 210707L, 229L, 1L, 4597L, 86L, 177936L, 189L, 10L, 22L)
)
data.table::setorder(Observed, TRT, sourceType)
data.table::setorder(Expected, TRT, sourceType)
if (!identical(Observed, Expected)) {
  stop("SSM.AUS.R: AUS source counts do not match the approved inventory.", call. = FALSE)
}

ObservedBranches <- DT[, .N, by = .(nModelBranches, branchVaries)]
ExpectedBranches <- data.table::data.table(
  nModelBranches = c(1L, 2L, 2L, 5L, 6L, 8L, 8L, 11L, 16L),
  branchVaries = c(0L, 0L, 1L, 0L, 0L, 0L, 1L, 0L, 0L),
  N = c(23915L, 362261L, 7349L, 1L, 3L, 2L, 1L, 418L, 53L)
)
data.table::setorder(ObservedBranches, nModelBranches, branchVaries)
if (!identical(ObservedBranches, ExpectedBranches)) {
  stop("SSM.AUS.R: AUS branch membership does not match the approved inventory.", call. = FALSE)
}

SourceCols <- c(
  "AreaSource", "PointSource", "SimpleFaultSource", "ComplexFaultSource"
)
AUX <- data.table::dcast(
  Observed, TRT ~ sourceType, value.var = "N", fill = 0L
)
data.table::setcolorder(AUX, c("TRT", SourceCols))
AUX <- data.table::rbindlist(list(
  AUX,
  AUX[, c(list(TRT = "Total"), lapply(.SD, sum)), .SDcols = SourceCols]
), use.names = TRUE)
AUX[, Total := as.integer(rowSums(.SD)), .SDcols = SourceCols]
data.table::setnames(
  AUX,
  SourceCols,
  c("Area", "Point", "SimpleFault", "ComplexFault")
)

TBL <- AUX |> buildTable(
  library          = "flextable",
  align.body       = "center",
  font.size.body   = FONT.SIZE.BODY,
  font.size.header = FONT.SIZE.HEADER
) |> flextable::set_table_properties(layout = "autofit")
TBL <- flextable::align(
  TBL,
  j = c("Area", "Point", "SimpleFault", "ComplexFault", "Total"),
  align = "right",
  part = "body"
)

rm(
  AUX, Classes, DATA, DT, Expected, ExpectedBranches,
  IdentityCols, IntrinsicCols, NormalizedProvider, Observed,
  ObservedBranches, Schema, SiteCount, SourceCols
)
# nolint end
