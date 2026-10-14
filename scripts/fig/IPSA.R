# nolint start
PLOT <- buildPlot(
  line.type     = "spline",
  plot.height   = 750,
  legend.layout = "horizontal",
  legend.show   = TRUE,
  xAxis.log     = TRUE,
  yAxis.log     = TRUE,
  xAxis.log.zero = TRUE,
  xAxis.log.zero.label = "PGA",
  xAxis.legend  = "Tn [s]",
  yAxis.legend  = sprintf("PSA(H1) [%s/s2]", SRS_UNITS),
  group.legend  = "ID",
  plot.theme    = NGR::hc_theme_538_gridlines(),
  data.lines    = SRS
)
# nolint end
