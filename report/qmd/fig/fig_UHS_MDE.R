
Caption <- CAP  |> sprintf(TR_TARGET,min(Vs30_TARGET),max(Vs30_TARGET),p_TARGET)
# Caption <- ""
UHS <- UHSTable[Vs30 %in% Vs30_TARGET & Vref==760 & TR == TR_TARGET & p==p_TARGET]
DATA <- UHS[,.(ID=paste0("Vs30 = ",Vs30," m/s"),Y=Sa,X=Tn)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "highcharter",
  yAxis.label =TRUE,
  plot.type="line",
  legend.layout="horizontal",
  legend.show=TRUE,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  line.size=THIN_LINE_SIZE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="Vs30 [m/s]",
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
