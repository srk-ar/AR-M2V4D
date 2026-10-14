# Comparison tables of the published products (combined by TR) against the
# Mw 7 generation: kmax (ensemble, p = mean) at each geometry's own relative
# targets and Dn (ensemble, p = mean) on the common ky grid, for every demand.
# Markdown to stdout: full per-cell tables for TR 10000 and MCE, summaries for
# every demand; CSV companions with every cell. Read-only on the products.
#   Rscript --vanilla compareTables2.R M7_DIR PUBLISHED_DIR MAP.csv OUT_DIR
suppressPackageStartupMessages(library(data.table))
ARGS <- commandArgs(trailingOnly = TRUE); stopifnot(length(ARGS) == 4L)
M7 <- ARGS[[1L]]; PUB <- ARGS[[2L]]; MAP <- fread(ARGS[[3L]], colClasses = "character"); OUTDIR <- ARGS[[4L]]
Contract <- jsonlite::read_json("newmark.json", simplifyVector = TRUE)
DaH <- as.numeric(Contract[["DaH.gmdp"]])
MwOf <- function(src) as.numeric(jsonlite::read_json(if (basename(src) == "newmark") "newmark.json" else paste0("newmark-", sub("^newmark-", "", basename(src)), ".json"), simplifyVector = TRUE)[["Mw.gmdp"]])
MAP[, Mw := vapply(source, MwOf, numeric(1))]
Shear <- readRDS(file.path(M7, "ShearTable.Rds"))
Heights <- unique(Shear[level == "mean", .(IDg, Hs)])
Targets <- Heights[, .(DaH = DaH, Da = signif(DaH * Hs, 6)), by = .(IDg, Hs)]
label <- function(ID, TR) fifelse(ID == "MCE", "MCE", as.character(TR))
# Relative difference in percent; a cell that is 0 in both generations is
# unchanged (0 %), a cell that is 0 only in one is undefined (NA).
pct <- function(a, b) fifelse(a == 0 & b == 0, 0, fifelse(a == 0, NA_real_, 100 * (b - a) / a))
DemandOrder <- c(MAP[demand != "MCE", as.character(sort(as.numeric(demand)))], "MCE")
pretty <- function(d) fifelse(d == "MCE", "MCE", paste0("TR ", d))

K7  <- readRDS(file.path(M7,  "kmaxTable.Rds"))[IDn == "ensemble" & p == "mean"]
KP  <- readRDS(file.path(PUB, "kmaxTable.Rds"))[IDn == "ensemble" & p == "mean"]
K <- merge(K7[, .(siteID, ID, TR, IDg, IDm, Da, kmax7 = kmax, PGA, beyond7 = beyond)],
           KP[, .(siteID, ID, TR, IDg, IDm, Da, kmaxNew = kmax, beyondNew = beyond)],
           by = c("siteID", "ID", "TR", "IDg", "IDm", "Da"))
K <- merge(K, Targets, by = c("IDg", "Da"))
K[, demand := label(ID, TR)]
K <- merge(K, MAP[, .(demand, Mw)], by = "demand")
K[, diffPct := pct(kmax7, kmaxNew)]
K[, demand := factor(demand, levels = DemandOrder)]
setorder(K, siteID, demand, IDg, IDm, DaH)
fwrite(K[, .(siteID, demand, Mw, IDg, Hs, IDm, DaH, Da, PGA, kmax7, kmaxNew, diffPct, beyond7, beyondNew)], file.path(OUTDIR, "kmax-compare.csv"))

D7 <- readRDS(file.path(M7,  "DnTable.Rds"))[IDn == "ensemble" & p == "mean"]
DP <- readRDS(file.path(PUB, "DnTable.Rds"))[IDn == "ensemble" & p == "mean"]
D <- merge(D7[, .(siteID, ID, TR, IDg, IDm, ky, Dn7 = Dn, Ts, Vs30)], DP[, .(siteID, ID, TR, IDg, IDm, ky, DnNew = Dn)],
           by = c("siteID", "ID", "TR", "IDg", "IDm", "ky"))
D[, demand := label(ID, TR)]
D <- merge(D, MAP[, .(demand, Mw)], by = "demand")
D[, diffPct := pct(Dn7, DnNew)]
D[, demand := factor(demand, levels = DemandOrder)]
setorder(D, siteID, demand, IDg, IDm, ky)
fwrite(D[, .(siteID, demand, Mw, IDg, IDm, Ts, Vs30, ky, Dn7, DnNew, diffPct)], file.path(OUTDIR, "dn-compare.csv"))

cell <- function(a, b, d, digits) fifelse(is.na(d), sprintf(paste0("%.", digits, "f / %.", digits, "f (n/d)"), a, b), sprintf(paste0("%.", digits, "f / %.", digits, "f (%+.1f%%)"), a, b, d))
printTable <- function(W) {
  cat("| ", paste(names(W), collapse = " | "), " |\n", sep = "")
  cat("|", paste(rep("---", ncol(W)), collapse = "|"), "|\n", sep = "")
  for (i in seq_len(nrow(W))) cat("| ", paste(unlist(W[i]), collapse = " | "), " |\n", sep = "")
}

cat("\n### Resumen por demanda: diferencia relativa (%) de kmax (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y Da/H\n\n")
S <- K[, .(min = min(diffPct, na.rm = TRUE), median = median(diffPct, na.rm = TRUE), max = max(diffPct, na.rm = TRUE), undefined = sum(is.na(diffPct)), zeros = sum(kmax7 == 0 & kmaxNew == 0)), by = .(demand, Mw, IDg)]
W <- dcast(S, demand + Mw ~ IDg, value.var = c("min", "median", "max"))
cat("| Demanda | Mw | ", paste(sort(unique(S$IDg)), collapse = " | "), " |\n", sep = "")
cat("|---|---|", paste(rep("---", uniqueN(S$IDg)), collapse = "|"), "|\n", sep = "")
for (d in DemandOrder) {
  X <- S[demand == d][order(IDg)]
  cat("| ", pretty(d), " | ", X$Mw[[1L]], " | ", paste(sprintf("[%.1f, %.1f, %.1f]", X$min, X$median, X$max), collapse = " | "), " |\n", sep = "")
}
cat("\nCeldas kmax con 0 en ambas generaciones (contadas como 0 %):", K[, sum(kmax7 == 0 & kmaxNew == 0)], "; celdas con 0 sólo en una (sin diferencia definida):", K[, sum(is.na(diffPct))], "\n")
cat("\n### Resumen por demanda: diferencia relativa (%) de Dn (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y los 30 ky\n\n")
S <- D[, .(min = min(diffPct, na.rm = TRUE), median = median(diffPct, na.rm = TRUE), max = max(diffPct, na.rm = TRUE), undefined = sum(is.na(diffPct)), zeros = sum(Dn7 == 0 & DnNew == 0)), by = .(demand, Mw, IDg)]
cat("| Demanda | Mw | ", paste(sort(unique(S$IDg)), collapse = " | "), " |\n", sep = "")
cat("|---|---|", paste(rep("---", uniqueN(S$IDg)), collapse = "|"), "|\n", sep = "")
for (d in DemandOrder) {
  X <- S[demand == d][order(IDg)]
  cat("| ", pretty(d), " | ", X$Mw[[1L]], " | ", paste(sprintf("[%.1f, %.1f, %.1f]", X$min, X$median, X$max), collapse = " | "), " |\n", sep = "")
}

for (DEM in c("10000", "MCE")) {
  Mw <- MAP[demand == DEM, Mw]
  cat("\n### kmax (ensemble, p = mean) [g], ", pretty(DEM), ": Mw 7 / Mw ", Mw, " (diferencia relativa)\n\n", sep = "")
  X <- K[demand == DEM]
  X[, cellText := cell(kmax7, kmaxNew, diffPct, 3L)]
  X[, DaHtxt := sprintf("Da/H %g%%", DaH)]
  W <- dcast(X, siteID + IDg + Hs + IDm ~ DaHtxt, value.var = "cellText")
  setcolorder(W, c("siteID", "IDg", "Hs", "IDm", paste0("Da/H ", sort(unique(X$DaH)), "%")))
  setorder(W, IDg, IDm); printTable(W)
}
KyGrid <- sort(unique(D$ky)); KySel <- KyGrid[c(1L, 6L, 11L, 16L, 21L, 26L, 30L)]
for (DEM in c("10000", "MCE")) {
  Mw <- MAP[demand == DEM, Mw]
  cat("\n### Dn (ensemble, p = mean) [cm], ", pretty(DEM), ": Mw 7 / Mw ", Mw, " (diferencia relativa), ky seleccionados de la grilla común\n\n", sep = "")
  X <- D[demand == DEM & ky %in% KySel]
  X[, cellText := cell(Dn7, DnNew, diffPct, 2L)]
  X[, kyTxt := sprintf("ky %.3f g", ky)]
  W <- dcast(X, siteID + IDg + IDm ~ kyTxt, value.var = "cellText")
  setcolorder(W, c("siteID", "IDg", "IDm", sprintf("ky %.3f g", KySel)))
  setorder(W, IDg, IDm); printTable(W)
}
cat("\nky grid (g):", paste(sprintf("%.4f", KyGrid), collapse = ", "), "\n")
