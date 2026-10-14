# Median Sa of each SCC model of the current tree at the governing cells.
suppressPackageStartupMessages(library(data.table))
G <- readRDS("data/hazard/tables/GMPETable.Rds")[TRT == "SCC" & dep == 15 & p == "0.50"]
G[, model := gsub("^\\[|\\]$", "", model)]
R <- sort(unique(G$Repi))
Rsel <- R[c(which.min(abs(R - 10)), which.min(abs(R - 20)), which.min(abs(R - 27)), which.min(abs(R - 50)))]
X <- G[Mw %in% c(5.5, 6.0, 6.5) & Repi %in% Rsel & Tn %in% c(0, 0.2, 1.0)]
for (TN in c(0, 0.2, 1.0)) {
  cat(sprintf("\n=== SCC median Sa [g], Tn = %s s, Vs30 760, dep 15 km; columns Repi [km]; last column = model / ensemble at Repi ~27 km ===\n", TN))
  W <- dcast(X[Tn == TN], model + Mw ~ round(Repi, 1), value.var = "Sa")
  E <- X[Tn == TN & model == "ensemble" & abs(Repi - 27) < 2, .(Mw, ens = Sa)]
  W <- merge(W, E, by = "Mw")
  W[, ratio27 := get(as.character(round(Rsel[3], 1))) / ens][, ens := NULL]
  setorder(W, Mw, model)
  print(W[, lapply(.SD, function(x) if (is.numeric(x)) signif(x, 3) else x)], nrows = 60)
}
