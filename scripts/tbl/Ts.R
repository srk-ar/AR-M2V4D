TBL <- DT |> buildTable(
    library = "flextable",
    align.body = "center",
    font.size.body = FONT.SIZE.BODY,
    font.size.header = FONT.SIZE.HEADER
) |> .mathHeader(c(
  Hs = "H_s",
  b = "b",
  s = "s",
  lo = "\\lambda_o",
  mo = "m_o",
  a1 = "a_1",
  Go = "G_o",
  VSo = "V_S^o",
  VS30 = "V_{S30}",
  Ts = "T_s"
)) |> flextable::set_table_properties(layout = "autofit")
rm(DT)
