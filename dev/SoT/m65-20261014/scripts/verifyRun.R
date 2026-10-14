# Step 4 verification: compare the M6.5 run (data/newmark-M65) with the
# current products (data/newmark). Read-only; prints observations.
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE)
ORIG <- if (length(ARGS) >= 1L) ARGS[[1L]] else "data/newmark"      # Mw 7 products
M65  <- if (length(ARGS) >= 2L) ARGS[[2L]] else "data/newmark-M65"  # run to verify
sha <- function(path) unname(tools::sha256sum(path))

cat("== ShearTable ==\n")
cat("sha orig:", sha(file.path(ORIG, "ShearTable.Rds")), "\n")
cat("sha M65 :", sha(file.path(M65,  "ShearTable.Rds")), "\n")

cat("\n== PGATable.csv ==\n")
cat("sha orig:", sha(file.path(ORIG, "M2V4D/CFD/PGATable.csv")), "\n")
cat("sha M65 :", sha(file.path(M65,  "M2V4D/CFD/PGATable.csv")), "\n")
P1 <- fread(file.path(ORIG, "M2V4D/CFD/PGATable.csv")); P2 <- fread(file.path(M65, "M2V4D/CFD/PGATable.csv"))
cat("identical content:", isTRUE(all.equal(P1, P2, check.attributes = FALSE)), "\n")

cmp <- function(name, keyCols, valueCol) {
  A <- readRDS(file.path(ORIG, name)); B <- readRDS(file.path(M65, name))
  cat("\n==", name, "==\n")
  cat("dim orig:", paste(dim(A), collapse = "x"), " dim M65:", paste(dim(B), collapse = "x"), "\n")
  cat("same names:", identical(names(A), names(B)), " same classes:", identical(sapply(A, class), sapply(B, class)),
      " same key:", identical(key(A), key(B)), "\n")
  cat("same attribute names:", identical(sort(names(attributes(A))), sort(names(attributes(B)))), "\n")
  J <- merge(A[, c(keyCols, valueCol), with = FALSE], B[, c(keyCols, valueCol), with = FALSE],
             by = keyCols, suffixes = c(".orig", ".m65"))
  cat("rows matched by key:", nrow(J), "of", nrow(A), "\n")
  J[, TRlabel := fifelse(is.na(TR), "MCE", as.character(TR))]
  x <- J[[paste0(valueCol, ".orig")]]; y <- J[[paste0(valueCol, ".m65")]]
  S <- J[, .(n = .N, nDiff = sum(abs(x[.I] - y[.I]) > 1e-12 * pmax(1, abs(x[.I]))),
             maxRel = max(abs(y[.I] - x[.I]) / pmax(abs(x[.I]), 1e-300))), by = .(ID, TRlabel)]
  print(S[order(ID, TRlabel)])
  invisible(J)
}
cmp("DnTable.Rds", c("siteID", "ID", "TR", "IDg", "IDm", "IDn", "p", "ky"), "Dn")
cmp("kmaxTable.Rds", c("siteID", "ID", "TR", "IDg", "IDm", "IDn", "p", "Da"), "kmax")
cmp("DnPlotTable.Rds", c("siteID", "ID", "TR", "IDg", "IDn", "p", "ky"), "Dn")

cat("\n== ky grids per cell identical between runs? ==\n")
A <- readRDS(file.path(ORIG, "DnTable.Rds")); B <- readRDS(file.path(M65, "DnTable.Rds"))
GA <- A[, .(ky = list(sort(unique(ky)))), by = .(siteID, ID, TR, IDg, IDm)]
GB <- B[, .(ky = list(sort(unique(ky)))), by = .(siteID, ID, TR, IDg, IDm)]
G <- merge(GA, GB, by = c("siteID", "ID", "TR", "IDg", "IDm"))
cat("cells:", nrow(G), " identical ky grids:", sum(mapply(identical, G$ky.x, G$ky.y)), "\n")
cat("one common grid across all cells (orig):", length(unique(GA$ky)) == 1L, "\n")

cat("\n== DnDraws: sampled PGA.s identical between runs (same random stream)? ==\n")
DA <- readRDS(file.path(ORIG, "M2V4D/CFD/DnDraws.Rds")); DB <- readRDS(file.path(M65, "M2V4D/CFD/DnDraws.Rds"))
cat("dim orig:", paste(dim(DA), collapse = "x"), " dim M65:", paste(dim(DB), collapse = "x"), " same key:", identical(key(DA), key(DB)), "\n")
KA <- DA[IDn == "AM88" & ky == min(ky), .(siteID, ID, TR, IDg, IDm, s, PGA.s, Dn)]
KB <- DB[IDn == "AM88" & ky == min(ky), .(siteID, ID, TR, IDg, IDm, s, PGA.s, Dn)]
K <- merge(KA, KB, by = c("siteID", "ID", "TR", "IDg", "IDm", "s"), suffixes = c(".orig", ".m65"))
K[, TRlabel := fifelse(is.na(TR), "MCE", as.character(TR))]
print(K[, .(n = .N, samePGAs = sum(PGA.s.orig == PGA.s.m65), sameDnAM88 = sum(Dn.orig == Dn.m65)), by = .(ID, TRlabel)][order(ID, TRlabel)])
KB2 <- DB[IDn == "BM19" & ky == min(ky), .(siteID, ID, TR, IDg, IDm, s, Dn)]
KA2 <- DA[IDn == "BM19" & ky == min(ky), .(siteID, ID, TR, IDg, IDm, s, Dn)]
K2 <- merge(KA2, KB2, by = c("siteID", "ID", "TR", "IDg", "IDm", "s"), suffixes = c(".orig", ".m65"))
K2[, TRlabel := fifelse(is.na(TR), "MCE", as.character(TR))]
print(K2[, .(n = .N, sameDnBM19 = sum(Dn.orig == Dn.m65), maxRel = max(abs(Dn.m65 - Dn.orig) / pmax(Dn.orig, 1e-300))), by = .(ID, TRlabel)][order(ID, TRlabel)])
rm(DA, DB); invisible(gc())
