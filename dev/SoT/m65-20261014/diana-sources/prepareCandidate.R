Root <- normalizePath(".")
Candidate <- file.path(Root, "dev/SoT/m65-20261014/diana-sources/candidate")
Files <- c("_local/gmdp.memo.en.qmd", "_chapters/dn.model.md",
           "_results/dn.results.qmd", "_results/dn.inputs.qmd")
for (FILE in Files) {
  Text <- readLines(file.path(Candidate, FILE))
  Text <- gsub("with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and", "with the reference magnitude assigned to each seismic demand and", Text, fixed = TRUE)
  Text <- gsub(
    "the reference magnitude of the project, $M_w=$ `r .fmt(Mw.gmdp, 1)`, is applied as a constant input to every demand, geometry, material and site evaluated",
    "the reference magnitude assigned to each seismic demand is applied to its geometry--material combinations",
    Text, fixed = TRUE
  )
  Text <- gsub(
    "Every formulation received the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` as a constant input and the demand of each of the",
    "Every formulation received the reference magnitude assigned to each seismic demand and the demand of each of the",
    Text, fixed = TRUE
  )
  Text <- gsub("k_h=\\frac{k_{\\max}}{\\mathrm{PGA} (V_{S30})}.", "k_h=100\\,\\frac{k_{\\max}}{\\mathrm{PGA} (V_{S30})}.", Text, fixed = TRUE)
  stopifnot(!any(grepl("Mw.gmdp", Text, fixed = TRUE)))
  if (FILE == "_local/gmdp.memo.en.qmd") {
    i <- match("## Performance-Based Seismic Coefficient {#sec-coefficients}", Text)
    stopifnot(!is.na(i))
    Text <- append(Text, c("", "{{< include /_results/dn.magnitudes.qmd >}}"), after = i)
  }
  if (FILE == "_results/dn.inputs.qmd") {
    Text <- c(Text, "", "{{< include /_results/dn.magnitudes.qmd >}}")
  }
  writeLines(Text, file.path(Candidate, FILE), useBytes = TRUE)
}
