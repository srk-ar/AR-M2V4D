library(data.table)
Root <- normalizePath(".")
Folder <- file.path(Root, "dev/SoT/m65-20261014/diana-hazard")
Baseline <- "/private/tmp/m2v4d-diana-hazard-baseline"
Site <- jsonlite::fromJSON("specs/sites/CFD.json")
Config <- jsonlite::fromJSON("hazard.json")
UHS <- readRDS("data/hazard/tables/UHSTable.Rds")
Accepted <- readRDS(file.path(Baseline, "UHSTable.Rds"))
stopifnot(fsetequal(Accepted, UHS[!Vs30 %in% c(220,580,910)], all = TRUE))
stopifnot(setequal(UHS$Vs30, Site$vs30), setequal(UHS$TR, Config[["TR.gmdp"]]),
          setequal(UHS$Tn, Accepted$Tn), setequal(UHS$p, Accepted$p),
          setequal(UHS$ID, Accepted$ID), setequal(UHS$branch, Accepted$branch))
stopifnot(!anyDuplicated(UHS, by = c("siteID", "ID", "Vs30", "TR", "Tn", "p")),
          nrow(UHS) == length(Site$vs30) * uniqueN(UHS$ID) * uniqueN(UHS$TR) * uniqueN(UHS$Tn) * uniqueN(UHS$p),
          all(is.finite(UHS$SaF)), all(UHS$SaF > 0), all(is.finite(UHS$Sa)), all(UHS$Sa > 0))
Quantiles <- UHS[p != "mean"]
Quantiles[, q := as.numeric(p)]
setorderv(Quantiles, c("ID", "siteID", "Vs30", "TR", "Tn", "q"))
stopifnot(all(Quantiles[, .(ordered = all(diff(SaF) >= 0)), by = .(ID, siteID, Vs30, TR, Tn)]$ordered))
Anchor <- dcast(UHS[Vs30 == 760], TR + Tn + p ~ branch, value.var = "SaF")
AnchorDifference <- max(abs(Anchor[["design-mixture"]] - Anchor[["oq-direct"]]),
                        abs(Anchor[["st20"]] - Anchor[["oq-direct"]]))
stopifnot(AnchorDifference == 0)
AEP <- readRDS("data/hazard/tables/AEPTable.Rds")
AcceptedAEP <- readRDS(file.path(Baseline, "AEPTable.Rds"))
stopifnot(fsetequal(AcceptedAEP, AEP[!Vs30 %in% c(220,580,910)], all = TRUE))
stopifnot(all(AEP$TR == 1/AEP$AEP))
for (File in setdiff(list.files(Baseline, pattern = "\\.Rds$"), c("UHSTable.Rds", "AEPTable.Rds", "UHSRock.Rds"))) {
  stopifnot(unname(tools::md5sum(file.path(Baseline, File))) == unname(tools::md5sum(file.path("data/hazard/tables", File))))
}
source("scripts/setup/hazardDiana.R")
Diana <- readDiana(Root)
Values <- dianaValues(Diana, Root)
stopifnot(all(Diana$aep[, .(ordered = all(diff(POE) <= 0)), by = .(Vs30,Tn,p)]$ordered))
Curves <- Diana$aep[, .(rows = .N, periods = uniqueN(Tn), intensities = uniqueN(Sa),
                       zero = sum(POE == 0), one = sum(POE == 1)), by = .(Vs30,p)]
stopifnot(all(Curves$periods == uniqueN(UHS$Tn)), all(Curves$intensities == 40))
Report <- list(uhsRows = nrow(UHS), oldUhsRowsExactlyPreserved = TRUE,
               oldAepRowsExactlyPreserved = TRUE, anchorMaximumDifference = AnchorDifference,
               quantilesOrdered = TRUE, otherProductsByteIdentical = TRUE,
               aepPoissonMaximumDifference = max(abs(AEP$POE - (1-exp(-AEP$AEP*AEP$ITo)))),
               directCurveCoverage = Curves, values = Values,
               tables = setNames(lapply(Diana$layout$tables, function(item) dianaTable(Diana, item)),
                                 vapply(Diana$layout$tables, function(item) item$label, character(1))))
jsonlite::write_json(Report, file.path(Folder, "product-verification.json"), pretty = TRUE, auto_unbox = TRUE, digits = NA)
message("Scientific product checks passed; baseline rows and independent products preserved")
