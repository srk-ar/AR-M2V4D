# The outer oqt attribute is shared by historical OQT and current Hazard tables.
.validateSSMProvenance <- function(data, file, model) {
  Meta <- attr(data, "oqt", exact = TRUE)
  Required <- c("producer", "written", "units", "keyRule", "selection", "engine", "inputs")
  if (!is.list(Meta) || !all(Required %in% names(Meta))) {
    stop(file, ": SSM inventory lacks required provenance.", call. = FALSE)
  }
  Version <- intersect(c("hazard", "oqt"), names(Meta))
  if (!length(Version)) {
    stop(file, ": SSM provenance identifies neither Hazard nor OQT.", call. = FALSE)
  }
  Patterns <- c(hazard = "^[0-9]+([.-][0-9]+)+$", oqt = "^[0-9a-f]{7,40}$")
  for (x in Version) {
    if (!is.character(Meta[[x]]) || length(Meta[[x]]) != 1L ||
        is.na(Meta[[x]]) || !grepl(Patterns[[x]], Meta[[x]])) {
      stop(file, ": invalid ", x, " identity in SSM provenance.", call. = FALSE)
    }
  }
  for (x in c("producer", "written", "engine")) {
    if (!is.character(Meta[[x]]) || length(Meta[[x]]) != 1L ||
        is.na(Meta[[x]]) || !nzchar(trimws(Meta[[x]]))) {
      stop(file, ": invalid ", x, " in SSM provenance.", call. = FALSE)
    }
  }
  if (!Meta$producer %in% c("ssm / runSSM.R", "ssm / aggregateSSM.R") ||
      !grepl("oq-3[.]26[.]2", Meta$engine) ||
      !identical(Meta$keyRule, paste0(
        "providerID normalized as in runAEPS.R so SSMTable joins AEPSTable ",
        "on (ID, siteID, providerID); SRMwTable keeps the raw sourceID and ",
        "needs consumer-side normalization"
      )) || !identical(Meta$selection,
        "complete: every source in the model, no distance cut and no ranking truncation")) {
    stop(file, ": SSM provenance is incomplete or incompatible.", call. = FALSE)
  }
  Units <- c(minMag = "Mw", maxMag = "Mw", usd = "km", lsd = "km")
  if (!identical(unname(Meta$units[names(Units)]), unname(Units))) {
    stop(file, ": SSM magnitude or depth units are incompatible.", call. = FALSE)
  }
  Sites <- unique(data$siteID)
  if (identical(Meta$producer, "ssm / runSSM.R")) {
    if (!identical(Meta$inputs, c(paste0("ssmLT_", model, ".xml"),
                                 paste(length(Sites), "sites")))) {
      stop(file, ": inventory provenance does not identify the ", model,
           " source model.", call. = FALSE)
    }
    return(invisible(NULL))
  }

  ModelID <- unique(data$ID)
  if (length(ModelID) != 1L || anyNA(c(ModelID, Sites)) ||
      any(!nzchar(c(ModelID, Sites)) | c(ModelID, Sites) %in% c(".", "..") |
          grepl("[/\\\\]", c(ModelID, Sites)))) {
    stop(file, ": aggregate model/site identity is invalid.", call. = FALSE)
  }
  Inputs <- Meta$inputs
  if (!is.character(Inputs) || anyNA(Inputs) || length(Inputs) != length(Sites)) {
    stop(file, ": aggregate inputs do not identify every site product.", call. = FALSE)
  }
  Inputs <- chartr("\\", "/", Inputs)
  Expected <- file.path(ModelID, Sites, "SSMTable.Rds")
  if (any(basename(dirname(dirname(dirname(Inputs)))) != "ssm") ||
      !setequal(file.path(basename(dirname(dirname(Inputs))),
                          basename(dirname(Inputs)), basename(Inputs)), Expected)) {
    stop(file, ": aggregate inputs do not match its model and sites.", call. = FALSE)
  }
  # The data root can move. Resolve recorded leaf identities under the current
  # table root, then verify their provenance and rows instead of trusting paths.
  for (Site in Sites) {
    FILE <- file.path(dirname(file), "ssm", ModelID, Site, "SSMTable.Rds")
    if (!file.exists(FILE)) {
      stop(file, ": required SSM site product not found: ", FILE, call. = FALSE)
    }
    Leaf <- readRDS(FILE)
    if (!inherits(Leaf, "data.frame") || !identical(names(Leaf), names(data)) ||
        !identical(unique(Leaf$ID), ModelID) ||
        !identical(unique(Leaf$siteID), Site) ||
        !identical(attr(Leaf, "oqt", exact = TRUE)$producer, "ssm / runSSM.R")) {
      stop(FILE, ": incompatible SSM site product.", call. = FALSE)
    }
    Leaf <- data.table::as.data.table(Leaf)
    .validateSSMProvenance(Leaf, file = FILE, model = model)
    AUX <- data[data$siteID == Site]
    if (!identical(lapply(AUX[order(providerID)], identity),
                   lapply(Leaf[order(providerID)], identity))) {
      stop(file, ": aggregate rows differ from site product: ", FILE, call. = FALSE)
    }
  }
  invisible(NULL)
}
