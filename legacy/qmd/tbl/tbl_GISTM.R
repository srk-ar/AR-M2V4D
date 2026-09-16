Category <- c("Low","Significant","High","Very High","Extreme")
OBE <- c("1:200","1:1,000","1:2,500","1:5,000","1:10,000")
MDE <- c("1:10,000","1:10,000","1:10,000","1:10,000","1:10,000")

DT <- data.table(
  "Category"=Category,
  "OBE"=OBE,
  "MDE"=MDE)
Caption <- "Annual Exceedance Probability (AEP) and Risk Categories according to the Global Industry Standard on Tailings Management (GISTM)"

TBL <- DT |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption)
