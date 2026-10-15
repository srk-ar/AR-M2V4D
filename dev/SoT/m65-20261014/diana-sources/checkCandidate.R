root <- normalizePath(".")
Candidate <- file.path(root, "dev/SoT/m65-20261014/diana-sources/candidate")
Evidence <- dirname(Candidate)
source(file.path(root, "scripts/setup/setup.R"))
DataRoot$newmark <- Candidate
Text <- knitr::knit(text = readLines(file.path(Candidate, "_results/dn.magnitudes.qmd")), quiet = TRUE)
writeLines(Text, file.path(Evidence, "magnitudes.md"))
stopifnot(!grepl("NA", Text, fixed = TRUE))
Files <- c("_local/gmdp.memo.en.qmd", "_chapters/dn.model.md",
           "_results/dn.results.qmd", "_results/dn.inputs.qmd")
CandidateText <- Text
BaselineText <- character()
BM.code <- "`BM19`"
Demands <- knitr::combine_words(prettyNum(sort(TR.gmdp), big.mark = ","), and = " and ")
Grid <- knitr::combine_words(.fmt(sort(DaH.gmdp), 2), and = " and ")
Equal <- TRUE
for (FILE in Files) {
  AUX <- readLines(file.path(root, FILE))
  BaselineText <- c(BaselineText, AUX[grepl("Mw.gmdp", AUX, fixed = TRUE)], "")
  AUX <- readLines(file.path(Candidate, FILE))
  stopifnot(!any(grepl("Mw.gmdp", AUX, fixed = TRUE)))
  AUX <- AUX[grepl("reference magnitude assigned", AUX, fixed = TRUE)]
  CandidateText <- c(CandidateText, knitr::knit(text = AUX, quiet = TRUE), "")
}
CandidateText <- c(CandidateText, "$$", "k_h=100\\,\\frac{k_{\\max}}{\\mathrm{PGA} (V_{S30})}.", "$${#eq-kh-normalization}")
writeLines(CandidateText, file.path(Evidence, "candidate.md"))
writeLines(BaselineText, file.path(Evidence, "baseline.md"))
stopifnot(identical(readBin(file.path(Candidate, "magnitude-map.csv"), "raw", n = file.info(file.path(Candidate, "magnitude-map.csv"))$size), readBin(file.path(root, "dev/SoT/m65-20261014/magnitude-map.csv"), "raw", n = file.info(file.path(root, "dev/SoT/m65-20261014/magnitude-map.csv"))$size)))
stopifnot(!any(grepl("[^ -~]", readLines(file.path(Evidence, "candidate.md")))))
message("Candidate clauses knitted; magnitude map byte-identical; English ASCII; no remaining scalar magnitude in the four admitted English sources.")
