DT <- ShearModelParameters[,-c("ModelID","GroupID","UN")] |> setnames(,old=c("NameID","AuthorID"),new=c("Material","Author")) |> setcolorder(c("Material","Author","A","Ce","n","emin","emax"))

Caption <- "Shear stiffness parameters for gravels, sands and fines"
TBL <- DT |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption)
