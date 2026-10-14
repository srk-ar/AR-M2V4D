# Combine the newmark products by return period from several runs, one per
# magnitude. The map is read from a CSV with columns demand,source: demand is
# a TR in years or "MCE"; source is a products directory. Every demand of the
# contract (TR.gmdp plus MCE) must be mapped exactly once. Preserves columns,
# column order, classes, key and attributes; publishes atomically into the
# target directory; writes a log CSV with rows per source and SHA-256.
#   Rscript --vanilla combine2.R MAP.csv TARGET_DIR LOG.csv
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE)
stopifnot(length(ARGS) == 3L)
MAP <- fread(ARGS[[1L]], colClasses = c(demand = "character", source = "character"))
TARGET <- ARGS[[2L]]; LOGFILE <- ARGS[[3L]]
Contract <- jsonlite::read_json("newmark.json", simplifyVector = TRUE)
Family <- sort(as.numeric(Contract[["TR.gmdp"]]))
Demands <- c(format(Family, scientific = FALSE, trim = TRUE), "MCE")
stopifnot(setequal(MAP$demand, Demands), !anyDuplicated(MAP$demand))
Sources <- unique(MAP$source)
sha <- function(path) unname(tools::sha256sum(path))
selectRows <- function(DT, demands) {
  TRs <- as.numeric(demands[demands != "MCE"])
  DT[(ID == "MCE" & "MCE" %in% demands) | (ID != "MCE" & TR %in% TRs)]
}
combineOne <- function(rel) {
  Tables <- lapply(Sources, function(src) readRDS(file.path(src, rel)))
  names(Tables) <- Sources
  Ref <- Tables[[1L]]
  for (DT in Tables) stopifnot(identical(names(DT), names(Ref)), identical(sapply(DT, class), sapply(Ref, class)),
                               identical(key(DT), key(Ref)), is.null(indices(DT)))
  Parts <- lapply(Sources, function(src) selectRows(Tables[[src]], MAP[source == src, demand]))
  names(Parts) <- Sources
  FixedRows <- !identical(basename(rel), "DnPlotTable.Rds")
  if (FixedRows) for (DT in Tables) stopifnot(nrow(DT) == nrow(Ref))
  OUT <- rbindlist(Parts, use.names = TRUE)
  setcolorder(OUT, names(Ref)); setkeyv(OUT, key(Ref))
  if (FixedRows) stopifnot(nrow(OUT) == nrow(Ref))
  stopifnot(identical(names(OUT), names(Ref)), identical(key(OUT), key(Ref)), identical(sapply(OUT, class), sapply(Ref, class)),
            identical(sort(names(attributes(OUT))), sort(names(attributes(Ref)))))
  for (src in Sources) {
    Dem <- MAP[source == src, demand]
    stopifnot(isTRUE(all.equal(selectRows(OUT, Dem), Parts[[src]], check.attributes = FALSE)))
  }
  list(table = OUT, rows = vapply(Parts, nrow, integer(1)))
}
publish <- function(DT, rel) {
  DEST <- file.path(TARGET, rel)
  TMP <- file.path(dirname(DEST), paste0(".", basename(DEST), ".tmp"))
  saveRDS(DT, TMP); file.rename(TMP, DEST); DEST
}
PRODUCTS <- c("M2V4D/CFD/DnDraws.Rds", "M2V4D/CFD/DnTable.Rds", "M2V4D/CFD/kmaxTable.Rds",
              "DnTable.Rds", "DnPlotTable.Rds", "kmaxTable.Rds")
LOG <- list()
for (REL in PRODUCTS) {
  before <- sha(file.path(TARGET, REL))
  R <- combineOne(REL)
  DEST <- publish(R$table, REL)
  BACK <- readRDS(DEST)
  stopifnot(identical(dim(BACK), dim(R$table)), identical(key(BACK), key(R$table)))
  LOG[[REL]] <- data.table(product = REL, source = names(R$rows), rows = unname(R$rows), total = nrow(R$table),
                           sha.before = before, sha.after = sha(DEST))
  cat(sprintf("%-28s %s  total %9d  sha %s -> %s\n", REL, paste(sprintf("%s=%d", basename(names(R$rows)), R$rows), collapse = " "),
              nrow(R$table), substr(before, 1, 12), substr(LOG[[REL]]$sha.after[[1L]], 1, 12)))
  rm(R, BACK); invisible(gc())
}
fwrite(rbindlist(LOG), LOGFILE)
cat("PGATable.csv:", sha(file.path(TARGET, "M2V4D/CFD/PGATable.csv")), "\nShearTable.Rds:", sha(file.path(TARGET, "ShearTable.Rds")), "\n")
