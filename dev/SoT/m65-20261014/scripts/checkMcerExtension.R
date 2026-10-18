# Acceptance of the mce/mcer/deq extension to Vs30 220, 580 and 910 (brief of
# 2026-10-17), without tolerances: the tables that must not change keep their
# SHA-256; MCETable, ASCETable and DEQTable now cover 11 Vs30 and every row
# that existed before is identical, column by column, to the previous copy.
#   Rscript --vanilla checkMcerExtension.R BEFORE_DIR SHA_TABLES SHA_NEWMARK
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE); stopifnot(length(ARGS) == 3L)
BEFORE <- ARGS[[1L]]; SHATABLES <- ARGS[[2L]]; SHANEWMARK <- ARGS[[3L]]
Ok <- TRUE
report <- function(label, pass) { cat(sprintf("%-70s %s\n", label, if (pass) "TRUE" else "FALSE")); if (!pass) Ok <<- FALSE }
shaOf <- function(path) unname(tools::sha256sum(path))
readSha <- function(file) { X <- fread(file, header = FALSE, sep = "\n")[[1L]]; setNames(sub(" .*$", "", X), sub("^[0-9a-f]+ +\\./", "", X)) }
# 1. Tables that must not change.
Before <- readSha(SHATABLES)
for (Name in c("UHSRock.Rds", "UHSTable.Rds", "AEPTable.Rds", "RMwTable.Rds", "AEPSTable.Rds", "GMPETable.Rds", "SSMTable.Rds"))
  report(paste("unchanged", Name), shaOf(file.path("data/hazard/tables", Name)) == Before[[Name]])
# 2. Newmark products unchanged.
NewmarkBefore <- readSha(SHANEWMARK)
for (Rel in names(NewmarkBefore)) report(paste("unchanged data/newmark/", Rel), shaOf(file.path("data/newmark", Rel)) == NewmarkBefore[[Rel]])
# 3. Extended tables: 11 Vs30 and previous rows identical.
Expected <- c(180, 220, 270, 360, 560, 580, 760, 800, 910, 1250, 1500)
checkExtended <- function(Name, previousRows) {
  Old <- readRDS(file.path(BEFORE, Name)); New <- readRDS(file.path("data/hazard/tables", Name))
  report(paste(Name, "columns and classes unchanged"), identical(names(Old), names(New)) && identical(sapply(Old, class), sapply(New, class)))
  report(paste(Name, "key unchanged"), identical(key(Old), key(New)))
  report(paste(Name, "Vs30 = 11 expected values"), identical(sort(unique(New$Vs30)), Expected))
  report(paste(Name, "previous row count", previousRows), nrow(Old) == previousRows)
  OldVs <- sort(unique(Old$Vs30)); Sub <- New[Vs30 %in% OldVs]
  report(paste(Name, "rows of the previous Vs30: same count"), nrow(Sub) == nrow(Old))
  setcolorder(Sub, names(Old)); setorderv(Old, names(Old)); setorderv(Sub, names(Sub))
  report(paste(Name, "rows of the previous Vs30: identical (all columns, no tolerance)"), isTRUE(all.equal(as.data.frame(Old), as.data.frame(Sub), tolerance = 0, check.attributes = FALSE)) && identical(as.data.frame(Old), as.data.frame(Sub)))
  report(paste(Name, "rows added only for 220/580/910"), nrow(New) - nrow(Old) == nrow(New[Vs30 %in% c(220, 580, 910)]))
  invisible(New)
}
Mce <- checkExtended("MCETable.Rds", 16576L)
Old760 <- readRDS(file.path(BEFORE, "MCETable.Rds"))[Vs30 == 760]; New760 <- Mce[Vs30 == 760]; setorderv(Old760, names(Old760)); setorderv(New760, names(New760))
report("MCETable rows at Vs30 760 identical to before (newmark input)", identical(as.data.frame(Old760), as.data.frame(New760)))
Asce <- checkExtended("ASCETable.Rds", 768L)
Deq <- checkExtended("DEQTable.Rds", 49152L)
cat("\nALL CHECKS PASSED:", Ok, "\n")
quit(status = if (Ok) 0L else 2L)
