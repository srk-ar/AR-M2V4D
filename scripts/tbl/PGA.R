# nolint start
TBL <- AUX |> buildTable(
  library          = "flextable",
  align.body       = "center",
  font.size.body   = FONT.SIZE.BODY,
  font.size.header = FONT.SIZE.HEADER
) |> .mathHeader(c(
  TR  = "T_R",
  PoE = "P_T"
)) |> flextable::set_table_properties(layout = "autofit")

if ("mean" %in% names(AUX)) {
  TBL <- flextable::bold(TBL, j = "mean", part = "body")
  TBL <- flextable::bold(TBL, j = "mean", part = "header")
}

rm(AUX)
# nolint end
