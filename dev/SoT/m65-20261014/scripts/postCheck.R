# Independent check of the published combination: every published table
# equals the Mw 7 snapshot (scratch backup) on TR 100..5000 and the Mw 6.5 run
# on TR 10000 and MCE, with the original schema, key and attributes.
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE)
BACKUP <- ARGS[[1L]]           # copy of data/newmark taken before combining
PUB <- "data/newmark"; M65 <- "data/newmark-M65"
KEEP.TR <- c(100, 200, 500, 1000, 2000, 2500, 5000)
PRODUCTS <- c("M2V4D/CFD/DnDraws.Rds", "M2V4D/CFD/DnTable.Rds", "M2V4D/CFD/kmaxTable.Rds",
              "DnTable.Rds", "DnPlotTable.Rds", "kmaxTable.Rds")
OK <- TRUE
for (REL in PRODUCTS) {
  P <- readRDS(file.path(PUB, REL)); A <- readRDS(file.path(BACKUP, REL)); B <- readRDS(file.path(M65, REL))
  same7  <- isTRUE(all.equal(P[ID != "MCE" & TR %in% KEEP.TR], A[ID != "MCE" & TR %in% KEEP.TR], check.attributes = FALSE))
  same65 <- isTRUE(all.equal(P[ID == "MCE" | TR == 10000], B[ID == "MCE" | TR == 10000], check.attributes = FALSE))
  schema <- identical(names(P), names(A)) && identical(sapply(P, class), sapply(A, class)) && identical(key(P), key(A)) &&
            identical(sort(names(attributes(P))), sort(names(attributes(A)))) && is.null(indices(P))
  # data.table keys sort in the C locale; re-keying a key-stripped copy must
  # reproduce the published row order exactly.
  X <- copy(P); setattr(X, "sorted", NULL); setkeyv(X, key(P))
  sorted <- isTRUE(all.equal(X, P)) && identical(attr(X, "sorted"), key(P))
  rm(X)
  byTR <- P[, .N, by = .(ID, TR)][order(ID, TR)]
  cat(sprintf("%-28s rows %9d  M7 block == backup: %s  M6.5 block == M65 run: %s  schema/key/attrs: %s  key order: %s\n",
              REL, nrow(P), same7, same65, schema, sorted))
  cat("   rows by ID,TR:", paste(sprintf("%s/%s=%d", byTR$ID, ifelse(is.na(byTR$TR), "NA", byTR$TR), byTR$N), collapse = " "), "\n")
  OK <- OK && same7 && same65 && schema && sorted
  rm(P, A, B); invisible(gc())
}
shaOf <- function(path) unname(tools::sha256sum(path))
pgaSame <- shaOf(file.path(PUB, "M2V4D/CFD/PGATable.csv")) == shaOf(file.path(BACKUP, "M2V4D/CFD/PGATable.csv"))
cat("\nPGATable.csv == backup:", pgaSame, "\n")
OK <- OK && pgaSame
shearSame <- shaOf(file.path(PUB, "ShearTable.Rds")) == shaOf(file.path(BACKUP, "ShearTable.Rds"))
cat("ShearTable.Rds == backup:", shearSame, "\n")
OK <- OK && shearSame
cat("\nALL CHECKS PASSED:", OK, "\n")
if (!OK) quit(status = 2)
