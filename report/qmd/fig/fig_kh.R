PGA_TARGET <- UHSTable[TR==TR_TARGET & Vref==760 & Vs30==Vs30_TARGET  & Tn==0]$PGA |> round(digits=3) |> unique()
# Name <- KIT[ID==ID_TARGET]$Name |> unique()
Caption <- CAP  |> sprintf(TR_TARGET,Vs30_TARGET,min(PGA_TARGET),max(PGA_TARGET),p_TARGET)

DATA <- KIT[Vs30==Vs30_TARGET & TR==TR_TARGET & p == p_TARGET,.(ID=paste0(Name,"- Vs30=",Vs30," m/s"),Y=Kh,X=Da)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "highcharter",
  yAxis.label =TRUE,
  plot.type="line",
  point.size = 0.1,
  legend.layout="horizontal",
  legend.valign = "bottom",
  legend.show=TRUE,
  xAxis.log = TRUE,
  yAxis.log = TRUE,
  line.size=THIN_LINE_SIZE,
  xAxis.legend="Da [cm]",
  yAxis.legend="Kh [% PGA]",
  group.legend="Facility",
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
