# nolint start
TBL <- AUX |> buildTable(
  library          = "flextable",
  align.body       = "center",
  font.size.body   = FONT.SIZE.BODY,
  font.size.header = FONT.SIZE.HEADER
) |> .mathHeader(c(
  TR = "T_R"
)) |> flextable::set_table_properties(layout = "autofit")

rm(AUX)
# nolint end
