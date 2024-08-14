Caption <- CAP  |> sprintf(min(TR_TARGET),max(TR_TARGET),Vs30_TARGET,p_TARGET)
# Caption <- ""
UHS <- UHSTable[Vs30==Vs30_TARGET & Vref==760 & TR %in% TR_TARGET]
DATA <- UHS[Vs30==Vs30_TARGET & p == p_TARGET,.(ID=paste0("TR= ",TR,"yr"),Y=Sa,X=Tn)][order(X)]|> unique()
DATA[X==0,X:=0.001]
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
  group.legend="TR [yr]",
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
