# nolint start
PLOT <- buildPlot(
  line.type     = "line",
  plot.height   = 750,
  legend.layout = "horizontal",
  legend.show   = TRUE,
  xAxis.legend  = "t [s]",
  yAxis.legend  = sprintf("%s(%s) [%s]", ID, DIR, Units),
  group.legend  = "ID",
  plot.theme    = NGR::hc_theme_538_gridlines(),
  data.lines    = SRS
)
PLOT$x$hc_opts$xAxis$gridLineWidth <- 0.3
PLOT$x$hc_opts$xAxis$gridLineColor <- "#e8e8e8"
PLOT$x$hc_opts$xAxis$minorGridLineWidth <- 0.15
PLOT$x$hc_opts$xAxis$minorGridLineColor <- "#f3f3f3"
PLOT$x$hc_opts$yAxis$gridLineWidth <- 0.3
PLOT$x$hc_opts$yAxis$gridLineColor <- "#e8e8e8"
PLOT$x$hc_opts$yAxis$minorGridLineWidth <- 0.15
PLOT$x$hc_opts$yAxis$minorGridLineColor <- "#f3f3f3"
PLOT$x$hc_opts$series <- lapply(PLOT$x$hc_opts$series, function(Series) {
  Series$visible <- FALSE
  Series
})
# nolint end
