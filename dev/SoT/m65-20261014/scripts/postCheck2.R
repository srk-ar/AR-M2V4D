# Independent check of a published by-TR combination against its map:
# every published table equals, demand by demand, the run the map assigns,
# with the schema, key, attributes and C-locale key order of the reference
# run; PGATable.csv and ShearTable.Rds equal the Mw 7 backup.
#   Rscript --vanilla postCheck2.R MAP.csv TARGET_DIR BACKUP_DIR
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE); stopifnot(length(ARGS) == 3L)
MAP <- fread(ARGS[[1L]], colClasses = c(demand = "character", source = "character"))
TARGET <- ARGS[[2L]]; BACKUP <- ARGS[[3L]]
selectRows <- function(DT, demands) {
  TRs <- as.numeric(demands[demands != "MCE"])
  DT[(ID == "MCE" & "MCE" %in% demands) | (ID != "MCE" & TR %in% TRs)]
}
PRODUCTS <- c("M2V4D/CFD/DnDraws.Rds", "M2V4D/CFD/DnTable.Rds", "M2V4D/CFD/kmaxTable.Rds",
              "DnTable.Rds", "DnPlotTable.Rds", "kmaxTable.Rds")
OK <- TRUE
for (REL in PRODUCTS) {
  P <- readRDS(file.path(TARGET, REL)); Ref <- readRDS(file.path(BACKUP, REL))
  schema <- identical(names(P), names(Ref)) && identical(sapply(P, class), sapply(Ref, class)) && identical(key(P), key(Ref)) &&
            identical(sort(names(attributes(P))), sort(names(attributes(Ref)))) && is.null(indices(P))
  X <- copy(P); setattr(X, "sorted", NULL); setkeyv(X, key(P))
  sorted <- isTRUE(all.equal(X, P)) && identical(attr(X, "sorted"), key(P)); rm(X)
  blocks <- character()
  nTotal <- 0L
  for (src in unique(MAP$source)) {
    Dem <- MAP[source == src, demand]
    S <- readRDS(file.path(src, REL))
    same <- isTRUE(all.equal(selectRows(P, Dem), selectRows(S, Dem), check.attributes = FALSE))
    nTotal <- nTotal + nrow(selectRows(P, Dem))
    blocks <- c(blocks, sprintf("%s[%s]=%s", basename(src), paste(Dem, collapse = ","), same))
    OK <- OK && same
    rm(S)
  }
  complete <- nTotal == nrow(P)
  byTR <- P[, .N, by = .(ID, TR)][order(ID, TR)]
  cat(sprintf("%-28s rows %9d  schema/key/attrs %s  key order %s  all rows mapped %s\n   blocks: %s\n   rows by ID,TR: %s\n",
              REL, nrow(P), schema, sorted, complete, paste(blocks, collapse = "  "),
              paste(sprintf("%s/%s=%d", byTR$ID, ifelse(is.na(byTR$TR), "NA", byTR$TR), byTR$N), collapse = " ")))
  OK <- OK && schema && sorted && complete
  rm(P, Ref); invisible(gc())
}
shaOf <- function(path) unname(tools::sha256sum(path))
pgaSame <- shaOf(file.path(TARGET, "M2V4D/CFD/PGATable.csv")) == shaOf(file.path(BACKUP, "M2V4D/CFD/PGATable.csv"))
shearSame <- shaOf(file.path(TARGET, "ShearTable.Rds")) == shaOf(file.path(BACKUP, "ShearTable.Rds"))
cat("\nPGATable.csv == backup:", pgaSame, "\nShearTable.Rds == backup:", shearSame, "\n")
OK <- OK && pgaSame && shearSame
cat("\nALL CHECKS PASSED:", OK, "\n")
if (!OK) quit(status = 2)
