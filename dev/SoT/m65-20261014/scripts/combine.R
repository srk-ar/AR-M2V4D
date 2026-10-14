# Step 6: combine the newmark products by return period.
#   TR 100..5000  -> data/newmark      (Mw 7, current products)
#   TR 10000, MCE -> data/newmark-M65  (Mw 6.5)
# Preserves columns, column order, classes, key and attributes of the
# original product. Publishes into data/newmark/ atomically (write to a
# temporary file in the same directory, then rename). Prints checks.
suppressPackageStartupMessages(library(data.table))
ORIG <- "data/newmark"; M65 <- "data/newmark-M65"
KEEP.TR <- c(100, 200, 500, 1000, 2000, 2500, 5000)
sha <- function(path) unname(tools::sha256sum(path))

combineOne <- function(rel) {
  A <- readRDS(file.path(ORIG, rel)); B <- readRDS(file.path(M65, rel))
  stopifnot(identical(names(A), names(B)), identical(sapply(A, class), sapply(B, class)),
            identical(key(A), key(B)), is.null(indices(A)), is.null(indices(B)))
  KEY <- key(A)
  A7  <- A[ID != "MCE" & TR %in% KEEP.TR]
  B65 <- B[ID == "MCE" | TR == 10000]
  # Every row of each source belongs to exactly one of the two TR blocks.
  stopifnot(nrow(A7) == nrow(A[!(ID == "MCE" | TR == 10000)]),
            nrow(B65) == nrow(B[!(ID != "MCE" & TR %in% KEEP.TR)]))
  # The cell grids are fixed for the draws, curves and coefficients, so the
  # row counts agree between runs; DnPlotTable omits Dn <= 1e-4 cm and its
  # row count depends on the values, so only its partition is checked.
  FixedRows <- !identical(basename(rel), "DnPlotTable.Rds")
  if (FixedRows) stopifnot(nrow(A7) + nrow(B65) == nrow(A), nrow(A) == nrow(B))
  OUT <- rbindlist(list(A7, B65), use.names = TRUE)
  setcolorder(OUT, names(A))
  setkeyv(OUT, KEY)
  # identity checks against the sources, row by row within each demand block
  stopifnot(nrow(OUT) == nrow(A7) + nrow(B65), identical(names(OUT), names(A)), identical(key(OUT), KEY),
            identical(sapply(OUT, class), sapply(A, class)))
  if (FixedRows) stopifnot(identical(dim(OUT), dim(A)))
  C7  <- OUT[ID != "MCE" & TR %in% KEEP.TR]; C65 <- OUT[ID == "MCE" | TR == 10000]
  stopifnot(isTRUE(all.equal(C7, A7, check.attributes = FALSE)), isTRUE(all.equal(C65, B65, check.attributes = FALSE)))
  # attributes: same names as the original (sorted = key, names, class, row.names, selfref)
  stopifnot(identical(sort(names(attributes(OUT))), sort(names(attributes(A)))))
  list(table = OUT, nA7 = nrow(A7), nB65 = nrow(B65))
}

publish <- function(DT, rel) {
  DEST <- file.path(ORIG, rel)
  TMP <- file.path(dirname(DEST), paste0(".", basename(DEST), ".tmp"))
  saveRDS(DT, TMP)
  file.rename(TMP, DEST)
  DEST
}

PRODUCTS <- c("M2V4D/CFD/DnDraws.Rds", "M2V4D/CFD/DnTable.Rds", "M2V4D/CFD/kmaxTable.Rds",
              "DnTable.Rds", "DnPlotTable.Rds", "kmaxTable.Rds")
LOG <- list()
for (REL in PRODUCTS) {
  before <- sha(file.path(ORIG, REL))
  R <- combineOne(REL)
  DEST <- publish(R$table, REL)
  BACK <- readRDS(DEST)
  stopifnot(identical(dim(BACK), dim(R$table)), identical(key(BACK), key(R$table)))
  LOG[[REL]] <- data.table(product = REL, rows.M7 = R$nA7, rows.M65 = R$nB65, rows = nrow(R$table),
                           sha.before = before, sha.after = sha(DEST))
  cat(sprintf("%-28s M7 rows %9d  M6.5 rows %9d  total %9d  sha %s -> %s\n", REL, R$nA7, R$nB65, nrow(R$table),
              substr(before, 1, 12), substr(LOG[[REL]]$sha.after, 1, 12)))
  rm(R, BACK); invisible(gc())
}
fwrite(rbindlist(LOG), "dev/SoT/m65-20261014/combine-log.csv")
cat("PGATable.csv untouched:", sha(file.path(ORIG, "M2V4D/CFD/PGATable.csv")), "\n")
cat("ShearTable.Rds untouched:", sha(file.path(ORIG, "ShearTable.Rds")), "\n")
