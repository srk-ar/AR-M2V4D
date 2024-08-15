Category <- c("Low","Significant","High A","High B","High C","Extreme")
OBE <- c("1:475","1:475","1:475 - 1:1,000","1:475 - 1:1,000","1:475 - 1:1,000","1:475 - 1:1,000")
MDE <- c("1:1,000","1:1,000","1:2,000","1:5,000","1:10,000","1:10,000")

DT <- data.table(
  "Category"=Category,
  "OBE"=OBE,
  "MDE"=MDE)
Caption <- "Annual Exceedance Probability (AEP) and Risk Categories according to the Australian National Committee on Large Dams (ANCOLD)"


TBL <- DT |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption)
