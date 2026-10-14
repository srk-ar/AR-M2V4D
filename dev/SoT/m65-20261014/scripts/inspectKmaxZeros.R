# Why does kmax reach a relative difference of 1 between runs? Read-only.
suppressPackageStartupMessages(library(data.table))
A <- readRDS("data/newmark/kmaxTable.Rds"); B <- readRDS("data/newmark-M65/kmaxTable.Rds")
KEY <- c("siteID", "ID", "TR", "IDg", "IDm", "IDn", "p", "Da")
J <- merge(A[, c(KEY, "kmax", "beyond"), with = FALSE], B[, c(KEY, "kmax", "beyond"), with = FALSE], by = KEY, suffixes = c(".7", ".65"))
J[, TRlabel := fifelse(is.na(TR), "MCE", as.character(TR))]
cat("rows with kmax == 0 (Mw 7):", sum(J$kmax.7 == 0), " (Mw 6.5):", sum(J$kmax.65 == 0), "\n")
J[, rel := abs(kmax.65 - kmax.7) / pmax(kmax.7, 1e-300)]
cat("rows with rel >= 0.5:", sum(J$rel >= 0.5), "\n")
print(J[rel >= 0.5, .N, by = .(zero7 = kmax.7 == 0, zero65 = kmax.65 == 0, IDn)][order(-N)])
print(J[rel >= 0.5 & kmax.7 > 0 & kmax.65 > 0][order(-rel)][1:5, .(ID, TRlabel, IDg, IDm, IDn, p, Da, kmax.7, kmax.65, beyond.7, beyond.65, rel)])
cat("\nensemble, p = mean rows: max rel =", J[IDn == "ensemble" & p == "mean", max(rel)], " zeros Mw7 =", J[IDn == "ensemble" & p == "mean", sum(kmax.7 == 0)], " zeros Mw6.5 =", J[IDn == "ensemble" & p == "mean", sum(kmax.65 == 0)], "\n")
cat("beyond rows (TRUE share): Mw7 =", mean(A$beyond > 0), " Mw6.5 =", mean(B$beyond > 0), "\n")
