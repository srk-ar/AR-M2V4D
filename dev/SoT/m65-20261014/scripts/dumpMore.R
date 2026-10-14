NS <- asNamespace("newmark")
for (NAME in c(".sampleDnScenario", ".drawDnModel", ".buildDnScenarioTable", "getDnTables", ".buildDnPlotTable", ".planProcess", "getDnKy")) {
  cat("==== newmark:::", NAME, " ====\n", sep = "")
  if (!exists(NAME, envir = NS, inherits = FALSE)) { cat("ABSENT\n\n"); next }
  LINES <- deparse(get(NAME, envir = NS), width.cutoff = 110L)
  cat(sprintf("%4d  %s\n", seq_along(LINES), LINES), sep = "")
  cat("\n")
}
