Root <- "/Users/averrik/Cloud/github/projects/AR-M2V4D"
setwd(Root)
Sys.setenv(PATH = paste("/usr/local/bin", Sys.getenv("PATH"), sep = .Platform$path.sep))
stopifnot(nzchar(Sys.which("quarto")))
Evidence <- file.path(Root, "dev/SoT/m65-20261014/diana-sources")
Masters <- c(memo = "_local/gmdp.memo.en.qmd", report = "_master/docx.en.qmd")
for (x in names(Masters)) {
  Log <- file.path(Evidence, paste0("render-", x, "-2.log"))
  Status <- system2("/usr/local/bin/ngr", c("render", Masters[[x]], "--profile", "docx"), stdout = Log, stderr = Log)
  writeLines(as.character(Status), file.path(Evidence, paste0("render-", x, "-2.exit")))
  if (Status != 0L) stop("NGR render failed: ", x, "; see ", Log)
}
