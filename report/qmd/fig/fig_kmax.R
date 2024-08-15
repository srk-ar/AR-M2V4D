PGA_TARGET <- UHSTable[TR==TR_TARGET  & p==p_TARGET & Tn==0 ]$PGA |> round(digits=4) |> unique()
Caption <- CAP  |> sprintf(TR_TARGET,min(Vs30_TARGET),max(Vs30_TARGET),min(PGA_TARGET),max(PGA_TARGET),p_TARGET)
# Caption <- ""
DATA <- KIT[ID==ID_TARGET & TR==TR_TARGET  & p == p_TARGET,.(ID=paste0(Name,"- Vs30=",Vs30," m/s"),Y=Kmax,X=Da)][order(X)]|> unique()

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
  yAxis.legend="Kmax [g]",
  group.legend="Facility",
  plot.theme = HC.THEME,
  data=DATA,
  plot.subtitle = Caption)
