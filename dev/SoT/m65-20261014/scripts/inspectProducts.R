# Read-only schema inspection of the current newmark products. Writes nothing.
suppressPackageStartupMessages(library(data.table))
.show <- function(path) {
  DT <- readRDS(path)
  cat("==== ", path, " ====\n", sep = "")
  cat("class:", paste(class(DT), collapse = ","), " dim:", paste(dim(DT), collapse = "x"), "\n")
  cat("key:", paste(key(DT), collapse = ","), " indices:", paste(indices(DT), collapse = ","), "\n")
  cat("attributes (non-standard):", paste(setdiff(names(attributes(DT)), c("names", "row.names", "class", ".internal.selfref", "sorted", "index")), collapse = ","), "\n")
  cat("columns:\n"); print(sapply(DT, function(x) class(x)[1L]))
  for (COL in intersect(c("ID", "TR", "siteID", "IDg", "IDm", "IDn", "p", "level", "Mw"), names(DT))) {
    V <- unique(DT[[COL]])
    cat(sprintf("  %-7s n=%d: %s\n", COL, length(V), paste(head(V, 12), collapse = ", ")))
  }
  if (all(c("ID", "TR") %in% names(DT))) {
    cat("rows by ID,TR:\n"); print(DT[, .N, by = .(ID, TR)][order(ID, TR)])
  }
  cat("\n")
}
.show("data/newmark/ShearTable.Rds")
.show("data/newmark/DnTable.Rds")
.show("data/newmark/kmaxTable.Rds")
.show("data/newmark/DnPlotTable.Rds")
.show("data/newmark/M2V4D/CFD/DnDraws.Rds")
PGA <- fread("data/newmark/M2V4D/CFD/PGATable.csv")
cat("==== PGATable.csv ====\n"); print(str(PGA)); print(PGA[, .N, by = .(ID, TR)][order(ID, TR)])
