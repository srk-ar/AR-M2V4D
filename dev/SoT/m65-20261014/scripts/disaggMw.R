# Mean and modal magnitude per return period from the project's own
# disaggregation table (hazard product). Read-only.
suppressPackageStartupMessages(library(data.table))
FILES <- c("data/hazard/disagg/M2V4D/CFD/RMwTable.Rds", "data/hazard/tables/RMwTable.Rds")
for (F in FILES) {
  DT <- readRDS(F)
  cat("==", F, "== dim", paste(dim(DT), collapse = "x"), " key:", paste(key(DT), collapse = ","), "\n")
  print(sapply(DT, class))
  for (COL in intersect(c("ID", "siteID", "Vs30", "Tn", "TR", "p"), names(DT))) {
    V <- sort(unique(DT[[COL]])); cat(sprintf("  %-6s n=%d: %s\n", COL, length(V), paste(head(V, 20), collapse = ", ")))
  }
}
DT <- readRDS(FILES[[1L]])
if ("siteID" %in% names(DT)) DT <- DT[siteID == "CFD"]
cat("\nMw bin width:", unique(round(diff(sort(unique(DT$Mw))), 4)), " R bin width:", unique(round(diff(sort(unique(DT$R))), 4))[1:3], "\n")
S <- DT[, {
  Tot <- sum(p)
  ByMw <- .SD[, .(p = sum(p)), by = Mw][order(Mw)]
  ByMw[, cum := cumsum(p) / Tot]
  .(MwMean = sum(p * Mw) / Tot, MwMode = ByMw[which.max(p), Mw], MwP50 = ByMw[cum >= 0.5, Mw][1L],
    MwP84 = ByMw[cum >= 0.84, Mw][1L], RMean = sum(p * R) / Tot, RMode = .SD[, .(p = sum(p)), by = R][which.max(p), R])
}, by = .(Tn, TR)][order(Tn, TR)]
cat("\n== Mean / modal / median / 84th-percentile Mw and mean / modal R per (Tn, TR), site CFD, from RMwTable ==\n")
print(S[, .(Tn, TR, MwMean = round(MwMean, 2), MwMode, MwP50, MwP84, RMean = round(RMean, 1), RMode)], nrows = 200)
fwrite(S, "dev/SoT/m65-20261014/disagg-Mw-by-TR.csv")
