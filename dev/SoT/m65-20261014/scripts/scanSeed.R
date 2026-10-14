NS <- asNamespace("newmark")
ALL <- ls(NS, all.names = TRUE)
FUNS <- ALL[vapply(ALL, function(n) is.function(get(n, envir = NS)), logical(1))]
callers <- function(pattern) {
  FUNS[vapply(FUNS, function(n) any(grepl(pattern, deparse(get(n, envir = NS)), fixed = TRUE)), logical(1))]
}
cat("callers of .dnSeed:", paste(callers(".dnSeed("), collapse = ", "), "\n")
cat("callers of fitDnProducts:", paste(callers("fitDnProducts("), collapse = ", "), "\n")
cat("callers of .runDnDemand:", paste(callers(".runDnDemand("), collapse = ", "), "\n")
cat("callers of fitKmaxProducts:", paste(callers("fitKmaxProducts("), collapse = ", "), "\n")
cat("functions mentioning set.seed:", paste(callers("set.seed("), collapse = ", "), "\n\n")
for (NAME in c(".runDnDemand", ".prepareDnScenario", ".drawDnModelCurve", callers(".dnSeed("))) {
  if (!exists(NAME, envir = NS, inherits = FALSE)) next
  cat("==== newmark:::", NAME, " ====\n", sep = "")
  LINES <- deparse(get(NAME, envir = NS), width.cutoff = 110L)
  cat(sprintf("%4d  %s\n", seq_along(LINES), LINES), sep = "")
  cat("\n")
}
