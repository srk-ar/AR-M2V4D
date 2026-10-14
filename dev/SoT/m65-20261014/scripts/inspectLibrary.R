# Read-only inspection of the installed newmark library, authorized by the
# owner's brief step 5: print the two builders and locate the seed and the
# inversion keys. Writes nothing.
cat("newmark version:", as.character(utils::packageVersion("newmark")), "\n")
cat("data.table version:", as.character(utils::packageVersion("data.table")), "\n\n")
NS <- asNamespace("newmark")
for (NAME in c("buildDnTables", "buildKmaxTable")) {
  cat("==== newmark:::", NAME, " ====\n", sep = "")
  if (!exists(NAME, envir = NS, inherits = FALSE)) {
    cat("ABSENT from namespace\n\n")
    next
  }
  LINES <- deparse(get(NAME, envir = NS), width.cutoff = 100L)
  cat(sprintf("%4d  %s\n", seq_along(LINES), LINES), sep = "")
  cat("\n")
}
cat("==== namespace objects matching seed|Seed|kmax|Kmax|Dn ====\n")
print(grep("seed|Seed|kmax|Kmax|buildDn|fitDn|invert", ls(NS, all.names = TRUE), value = TRUE))
