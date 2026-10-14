# nolint start
# Deterministic scenario means and MCE envelopes, per Tn.
# The canonical MCETable ID "MCE" supplies the mean and p = 0.84
# deterministic envelopes; the legacy ID "max" is not consumed here.
if (!exists("Vs30.target", inherits = FALSE) || length(Vs30.target) != 1L) Vs30.target <- 760

SITE_ID <- if (exists("siteID.target", inherits = FALSE)) siteID.target else {
  unique(MCETable[!is.na(siteID) & nzchar(siteID), siteID])
}
if (length(SITE_ID) != 1L) stop("DSHA.R: set siteID.target to one siteID.", call. = FALSE)

SCN <- sort(unique(MCETable[
  !ID %in% c("MCE", "max", "min") & !grepl("\\.(site|oq|max)$", ID) &
    siteID %in% SITE_ID, ID
]))
TNS <- intersect(c(0, 0.1, 0.2, 0.5, 1, 2, 5), unique(MCETable$Tn))

DT <- rbindlist(list(
  MCETable[
    ID %in% SCN & siteID %in% SITE_ID & Vs30 == Vs30.target &
      .matchP(p, "mean") & Tn %in% TNS,
    .(Tn, col = ID, DSHA = SaF)
  ],
  MCETable[
    ID == "MCE" & siteID %in% SITE_ID & Vs30 == Vs30.target &
      .matchP(p, c("mean", "0.84")) & Tn %in% TNS,
    .(Tn, col = fifelse(.matchP(p, "mean"), "MCE", "MCE (84%)"), DSHA = SaF)
  ]
), use.names = TRUE)
if (!nrow(DT)) stop("DSHA.R: no rows for the selected site/Vs30.", call. = FALSE)
if (PSA_Units %in% c("cm", "cm/s2", "cm/s**2", "cm/s^2")) DT[, DSHA := round(DSHA * 980.665, 0)]
if (PSA_Units %in% c("g"))                                DT[, DSHA := round(DSHA, 3)]

AUX <- dcast(DT, Tn ~ col, value.var = "DSHA")
COLS <- intersect(
  c("Tn", SCN, "MCE", "MCE (84%)"),
  names(AUX)
)
setcolorder(AUX, COLS)

TBL <- AUX |> buildTable(
  library          = "flextable",
  align.body       = "center",
  font.size.body   = FONT.SIZE.BODY,
  font.size.header = FONT.SIZE.HEADER
) |> .mathHeader(c(Tn = "T_n")) |> flextable::set_table_properties(layout = "autofit")
TBL <- flextable::bold(TBL, j = intersect(c("MCE", "MCE (84%)"), names(AUX)), part = "header")

rm(DT, AUX, COLS, SCN, TNS, SITE_ID)
# nolint end
