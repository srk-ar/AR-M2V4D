# nolint start
DT <- kmaxTable[
  siteID %in% siteID.target & IDg %in% IDg.target & IDm %in% IDm.target &
    ID == "MCE" & IDn == "ensemble" & .matchP(p, "mean")
]
MASK <- .markExtrapolation(DT, DT$kmax, .currentTarget("KyLimits.kmax"))
DT <- DT[, .(siteID, IDg, Da, Kh, extrapolated = MASK)]
AUX <- unique(ShearTable[IDg %in% IDg.target, .(IDg, Hs)])
DT <- AUX[DT, on = "IDg"]
DT[, DaH := signif(Da / Hs, 3L)]
DT <- DT[DaH %in% signif(DAMAGE.CUTS, 3L),
  .(Kh = paste0(
    .fmt(round(100 * min(Kh), 1L), 1L), "–",
    .fmt(round(100 * max(Kh), 1L), 1L)
  ), extrapolated = any(extrapolated)), by = .(siteID, Hs, DaH)]
MASK <- dcast(DT, siteID + Hs ~ DaH, value.var = "extrapolated")
DT <- dcast(DT, siteID + Hs ~ DaH, value.var = "Kh")
IDX <- DT[, order(match(siteID, siteID.target), Hs)]
DT <- DT[IDX]
MASK <- MASK[IDX, !c("siteID", "Hs")]

TBL <- DT |> buildTable(
  library          = "flextable",
  align.body       = "center",
  font.size.body   = FONT.SIZE.BODY,
  font.size.header = FONT.SIZE.HEADER
) |> .mathHeader(c(Hs = "H_s")) |>
  .markTable(MASK) |>
  .damageTable(DAMAGE.CUTS, DAMAGE.COLORS) |>
  flextable::set_table_properties(layout = "autofit")

rm(DT, AUX, MASK, IDX)
# nolint end
