library(data.table)
DT <- data.table(
  "Tectonic Type" = c("B", "B", "B", "B", "A", "A", "D", "D", "D", "D", "C", "C", "C", "C", "E", "E"),
  "Model ID" = c("AkkarEtAlRjb2014", "PezeshkEtAl2011NEHRPBC", "AtkinsonBoore2006Modified2011", "ChiouYoungs2014","AkkarEtAlRjb2014", "ChiouYoungs2014","AkkarEtAlRjb2014", "PezeshkEtAl2011NEHRPBC", "AtkinsonBoore2006Modified2011", "ChiouYoungs2014","AkkarEtAlRjb2014", "PezeshkEtAl2011NEHRPBC", "AtkinsonBoore2006Modified2011", "ChiouYoungs2014","PezeshkEtAl2011NEHRPBC","AtkinsonBoore2006Modified2011"),
  "Model Weight" = c(0.375, 0.125, 0.125, 0.375,0.5, 0.5,0.125, 0.375, 0.375, 0.125,0.25, 0.25, 0.25, 0.25,0.5, 0.5)
)

Caption <- "Ground Motion Model (GMM) logic-tree for Central Asia (CEA)"


TBL <- DT |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption)
