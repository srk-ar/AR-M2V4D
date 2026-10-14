# Step 7 tables: kmax (ensemble, p = mean) and Dn (ensemble, p = mean) for
# TR 10000 and MCE, Mw 7 (data/newmark before combining, read from the
# sha-before snapshot copy) against Mw 6.5 (data/newmark-M65), with relative
# differences. Writes CSV companions and prints Markdown tables. Read-only on
# the products.
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE)
M7  <- if (length(ARGS) >= 1L) ARGS[[1L]] else "data/newmark"
M65 <- if (length(ARGS) >= 2L) ARGS[[2L]] else "data/newmark-M65"
OUTDIR <- "dev/SoT/m65-20261014"
Contract <- jsonlite::read_json("newmark.json", simplifyVector = TRUE)
DaH <- as.numeric(Contract[["DaH.gmdp"]])

Shear <- readRDS(file.path(M7, "ShearTable.Rds"))
Heights <- unique(Shear[level == "mean", .(IDg, Hs)])

label <- function(ID, TR) fifelse(ID == "MCE", "MCE", paste0("TR ", TR))
pct <- function(a, b) 100 * (b - a) / a

# ---- kmax: ensemble, p = mean, each geometry at its own relative targets ----
K7  <- readRDS(file.path(M7,  "kmaxTable.Rds"))[IDn == "ensemble" & p == "mean" & (ID == "MCE" | TR == 10000)]
K65 <- readRDS(file.path(M65, "kmaxTable.Rds"))[IDn == "ensemble" & p == "mean" & (ID == "MCE" | TR == 10000)]
Targets <- Heights[, .(DaH = DaH, Da = signif(DaH * Hs, 6)), by = .(IDg, Hs)]
K <- merge(K7[, .(siteID, ID, TR, IDg, IDm, Da, kmax7 = kmax, PGA, beyond7 = beyond)],
           K65[, .(siteID, ID, TR, IDg, IDm, Da, kmax65 = kmax, beyond65 = beyond)],
           by = c("siteID", "ID", "TR", "IDg", "IDm", "Da"))
K <- merge(K, Targets, by = c("IDg", "Da"))
K[, `:=`(demand = label(ID, TR), diffPct = pct(kmax7, kmax65))]
setorder(K, siteID, ID, -TR, IDg, IDm, DaH)
fwrite(K[, .(siteID, demand, IDg, Hs, IDm, DaH, Da, PGA, kmax7, kmax65, diffPct, beyond7, beyond65)],
       file.path(OUTDIR, "kmax-compare.csv"))

# ---- Dn: ensemble, p = mean, on the common ky grid ----
D7  <- readRDS(file.path(M7,  "DnTable.Rds"))[IDn == "ensemble" & p == "mean" & (ID == "MCE" | TR == 10000)]
D65 <- readRDS(file.path(M65, "DnTable.Rds"))[IDn == "ensemble" & p == "mean" & (ID == "MCE" | TR == 10000)]
D <- merge(D7[, .(siteID, ID, TR, IDg, IDm, ky, Dn7 = Dn, Ts, Vs30)],
           D65[, .(siteID, ID, TR, IDg, IDm, ky, Dn65 = Dn)],
           by = c("siteID", "ID", "TR", "IDg", "IDm", "ky"))
D[, `:=`(demand = label(ID, TR), diffPct = pct(Dn7, Dn65))]
setorder(D, siteID, ID, -TR, IDg, IDm, ky)
fwrite(D[, .(siteID, demand, IDg, IDm, Ts, Vs30, ky, Dn7, Dn65, diffPct)], file.path(OUTDIR, "dn-compare.csv"))

# ---- Markdown ----
cell <- function(a, b, d, digits) sprintf(paste0("%.", digits, "f / %.", digits, "f (%+.1f%%)"), a, b, d)
mdTable <- function(DT, rowCols, colCol, valueFun, header) {
  Cols <- sort(unique(DT[[colCol]]))
  W <- dcast(DT, as.formula(paste(paste(rowCols, collapse = " + "), "~", colCol)), value.var = "cellText")
  cat("| ", paste(c(rowCols, header(Cols)), collapse = " | "), " |\n", sep = "")
  cat("|", paste(rep("---", length(rowCols) + length(Cols)), collapse = "|"), "|\n", sep = "")
  for (i in seq_len(nrow(W))) cat("| ", paste(unlist(W[i]), collapse = " | "), " |\n", sep = "")
}

cat("\n## kmax (ensemble, p = mean) [g]: Mw 7 / Mw 6.5 (diferencia relativa)\n")
for (DEM in c("TR 10000", "MCE")) {
  cat("\n### ", DEM, "\n\n", sep = "")
  X <- K[demand == DEM]
  X[, cellText := cell(kmax7, kmax65, diffPct, 3L)]
  X[, DaHtxt := sprintf("Da/H %g%%", DaH)]
  X[, DaHord := DaH]
  W <- dcast(X, siteID + IDg + Hs + IDm ~ DaHtxt, value.var = "cellText")
  Order <- paste0("Da/H ", sort(unique(X$DaH)), "%")
  setcolorder(W, c("siteID", "IDg", "Hs", "IDm", Order))
  setorder(W, IDg, IDm)
  cat("| ", paste(names(W), collapse = " | "), " |\n", sep = "")
  cat("|", paste(rep("---", ncol(W)), collapse = "|"), "|\n", sep = "")
  for (i in seq_len(nrow(W))) cat("| ", paste(unlist(W[i]), collapse = " | "), " |\n", sep = "")
  cat("\nResumen de la diferencia relativa (%) por geometría: ")
  S <- X[, .(min = min(diffPct), median = median(diffPct), max = max(diffPct)), by = IDg][order(IDg)]
  cat(paste(sprintf("%s [%.1f, %.1f, %.1f]", S$IDg, S$min, S$median, S$max), collapse = "; "), "\n")
}

cat("\n## Dn (ensemble, p = mean) [cm]: Mw 7 / Mw 6.5 (diferencia relativa), ky seleccionados de la grilla común\n")
KyGrid <- sort(unique(D$ky))
KySel <- KyGrid[c(1L, 6L, 11L, 16L, 21L, 26L, 30L)]
for (DEM in c("TR 10000", "MCE")) {
  cat("\n### ", DEM, "\n\n", sep = "")
  X <- D[demand == DEM & ky %in% KySel]
  X[, cellText := cell(Dn7, Dn65, diffPct, 2L)]
  X[, kyTxt := sprintf("ky %.3f g", ky)]
  W <- dcast(X, siteID + IDg + IDm ~ kyTxt, value.var = "cellText")
  setcolorder(W, c("siteID", "IDg", "IDm", sprintf("ky %.3f g", KySel)))
  setorder(W, IDg, IDm)
  cat("| ", paste(names(W), collapse = " | "), " |\n", sep = "")
  cat("|", paste(rep("---", ncol(W)), collapse = "|"), "|\n", sep = "")
  for (i in seq_len(nrow(W))) cat("| ", paste(unlist(W[i]), collapse = " | "), " |\n", sep = "")
  cat("\nResumen de la diferencia relativa (%) sobre los 30 ky por geometría: ")
  S <- D[demand == DEM, .(min = min(diffPct), median = median(diffPct), max = max(diffPct)), by = IDg][order(IDg)]
  cat(paste(sprintf("%s [%.1f, %.1f, %.1f]", S$IDg, S$min, S$median, S$max), collapse = "; "), "\n")
}
cat("\nky grid (g):", paste(sprintf("%.4f", KyGrid), collapse = ", "), "\n")
