# nolint start
PLOT <- buildPlot(
  line.type     = "spline",
  plot.height   = 750,
  legend.layout = "horizontal",
  legend.show   = TRUE,
  xAxis.log     = TRUE,
  yAxis.log     = TRUE,
  xAxis.log.zero = ID == "PSA",
  xAxis.log.zero.label = "PGA",
  xAxis.legend  = "Tn [s]",
  yAxis.legend  = sprintf("%s(%s) [%s]", ID, DIR, Units),
  group.legend  = "ID",
  plot.theme    = NGR::hc_theme_538_gridlines(),
  fill.legend   = if (exists("SRS_TARGET_FILL_LEGEND", inherits = TRUE)) {
    SRS_TARGET_FILL_LEGEND
  } else {
    "min–max"
  },
  fill.min.style = "Dash",
  fill.min.size = THIN_LINE_SIZE,
  fill.max.style = "Dash",
  fill.max.size = THIN_LINE_SIZE,
  data.lines    = SRS
)
# nolint end
