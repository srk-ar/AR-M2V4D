NS <- asNamespace("newmark")
NAMES <- c(".seedInteger", ".dnSeed", "fitDnProducts", ".buildDnRecords",
           ".fitDnScenarioPrepared", ".fitDnCurvePrepared", "fitDnScenarios", "fitDnScenario",
           "fitKmaxProducts", ".buildKmaxRecords", ".buildKmaxDraws", ".aggregateKmaxDraws",
           ".fitKmaxCell", "fitKmaxScenarios", "fitKmaxScenario", "invertDnDraws", "getKmaxTable")
for (NAME in NAMES) {
  cat("==== newmark:::", NAME, " ====\n", sep = "")
  if (!exists(NAME, envir = NS, inherits = FALSE)) { cat("ABSENT\n\n"); next }
  LINES <- deparse(get(NAME, envir = NS), width.cutoff = 110L)
  cat(sprintf("%4d  %s\n", seq_along(LINES), LINES), sep = "")
  cat("\n")
}
