TR_max <- 500000
AEP <- AEPTable[p == p_TARGET & Tn %in% Tn_TARGET & TR<=TR_max & Vs30==Vs30_TARGET & Vref==760]
Caption <- CAP  |> sprintf(min(Tn_TARGET),max(Tn_TARGET),Vs30_TARGET,p_TARGET)
DATA <- AEP[ ,.(ID=paste0("Tn= ",Tn," s"),X=Sa,Y=AEP)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "highcharter",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="line",
  legend.layout="horizontal",
  legend.show=TRUE,
  line.size=THIN_LINE_SIZE,
  xAxis.log = TRUE,
  yAxis.log = TRUE,
  yAxis.legend="AEP [1/yr]",
  xAxis.legend="Sa(Tn) [g]",
  group.legend="Tn [s]",
  plot.theme = HC.THEME,
  data=DATA,
  plot.subtitle = Caption)



if(!knitr::is_html_output()){
  FILE <- tempfile(tmpdir = imagesFolder,pattern="fig",fileext=".png")
  XDELAY <- max(DELAY,round(nrow(DT)/1500*DELAY,digits = 2))
  AUX <- tempfile(pattern="fig",fileext=".html")
  htmlwidgets::saveWidget(widget = PLOT,background=params$background, file = AUX,selfcontained = TRUE)
  webshot2::webshot(delay=XDELAY,url = AUX, file = FILE)
  FIG <- knitr::include_graphics(path=FILE)
} else {
  FIG <- PLOT
}
