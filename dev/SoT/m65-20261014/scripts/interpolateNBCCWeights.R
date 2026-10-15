# Extend the SCC NBCC seed with period-dependent weights at every period of
# the house grid, interpolated in log(T) from the official nodes. The eleven
# official IMTs keep their weights untouched; the AA13 branches keep their
# base weights. Interpolated weights are written with six decimals and the
# rounding residual of each period goes to its largest weight, so the thirteen
# NGA-East weights sum to exactly 0.5 per period (OpenQuake tolerance 1e-7).
# Writes the seed in place; the official-node version remains in
# gmmLT_NBCC.xml.bak. Usage: Rscript interpolateNBCCWeights.R SEED.xml
suppressPackageStartupMessages(library(xml2))
ARGS <- commandArgs(trailingOnly = TRUE)
FILE <- ARGS[[1L]]
HOUSE <- c(0.05, 0.075, 0.10, 0.12, 0.15, 0.18, 0.20, 0.22, 0.25, 0.28, 0.30, 0.35, 0.40, 0.45, 0.50,
           0.60, 0.70, 0.75, 0.85, 0.90, 1.00, 1.25, 1.50, 1.75, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00)
MICRO <- 1e6
DOC <- read_xml(FILE)
NS <- c(n = "http://openquake.org/xmlns/nrml/0.4")
Branches <- xml_find_all(DOC, ".//n:logicTreeBranch", NS)
imtLabel <- function(t) paste0("SA(", format(t, trim = TRUE, drop0trailing = TRUE), ")")
periodOf <- function(label) as.numeric(sub("^SA\\((.*)\\)$", "\\1", label))
# First pass: interpolate every NGA-East branch at the missing periods.
Nodes <- NULL; Missing <- NULL; Rows <- list(); Target <- list()
for (i in seq_along(Branches)) {
  B <- Branches[[i]]
  W <- xml_find_all(B, "./n:uncertaintyWeight", NS)
  IMT <- xml_attr(W, "imt")
  SA <- which(!is.na(IMT) & startsWith(IMT, "SA("))
  if (!length(SA)) next                      # AA13 branches: base weight only, left as they are
  T0 <- periodOf(IMT[SA]); V0 <- as.numeric(xml_text(W[SA]))
  O <- order(T0); T0 <- T0[O]; V0 <- V0[O]
  if (is.null(Nodes)) {
    Nodes <- T0
    Missing <- HOUSE[!sapply(HOUSE, function(t) any(abs(T0 - t) < 1e-9))]
    stopifnot(all(Missing > min(T0) & Missing < max(T0)))
  } else stopifnot(identical(Nodes, T0))
  Target[[length(Target) + 1L]] <- i
  Rows[[length(Rows) + 1L]] <- round(approx(log(T0), V0, xout = log(Missing))$y * MICRO)
}
M <- do.call(rbind, Rows)                    # integer micro-units, branches x missing periods
stopifnot(nrow(M) == 13L)
# Residual per period to the largest weight, so each column sums to 0.5 exactly.
for (j in seq_len(ncol(M))) { Res <- 0.5 * MICRO - sum(M[, j]); k <- which.max(M[, j]); M[k, j] <- M[k, j] + Res }
stopifnot(all(colSums(M) == 0.5 * MICRO))
# Second pass: write the entries.
for (r in seq_len(nrow(M))) {
  B <- Branches[[Target[[r]]]]
  for (j in seq_along(Missing)) {
    E <- xml_add_child(B, "uncertaintyWeight", sprintf("%.6f", M[r, j] / MICRO))
    xml_set_attr(E, "imt", imtLabel(Missing[j]))
  }
}
write_xml(DOC, FILE)
cat("official SA nodes:", paste(Nodes, collapse = " "), "\n")
cat("branches extended:", nrow(M), " periods added per branch:", ncol(M), "\n")
cat("branch 01 interpolated weights:\n"); print(setNames(M[1, ] / MICRO, imtLabel(Missing)))
