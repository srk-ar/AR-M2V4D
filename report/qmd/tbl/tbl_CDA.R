
Category <- c("Low","Significant","High","Very High","Extreme")
OBE <- c("1:100","1:100 - 1:1,1000","1:2,475","1:2,475 - 1:10,000","1:10,000")
MDE <- c("1:1,000","1:2,475","1:2,475 - 1:10,000","1:10,000","1:10,000")

DT <- data.table(
  "Category"=Category,
  "OBE"=OBE,
  "MDE"=MDE)
Caption <- "Annual Exceedance Probability (AEP) and Risk Categories according to Canadian Dam Association (CDA)"


TBL <- DT |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption)
