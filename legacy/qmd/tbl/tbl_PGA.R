Caption <- CAP  |> sprintf(min(TR_TARGET),max(TR_TARGET),min(Vs30_TARGET),max(Vs30_TARGET),p_TARGET)
# Caption <- ""

UHS <- UHSTable[p == p_TARGET & Vs30 %in% Vs30_TARGET & TR %in% TR_TARGET ]

# DT <- gmdp::buildTable.Sa(UHS,Tno=0,po=p_TARGET,TRo = TR_TARGET,Vs30o = Vs30_TARGET,tagUnits = FALSE)
DT <- UHS[Tn==0 & TR%in%TR_TARGET & Vs30%in%Vs30_TARGET,.(Tn,TR,p,PGA,Vs30,SID)]
DT[,`:=`(PGA=round(PGA,4),POE=round(100*(1-exp(-50/TR)),1))]
AUX <- dcast(DT[,.(TR,Vs30,PGA,POE,p)], TR+POE+p   ~ Vs30, value.var = "PGA",fun.aggregate=mean)
setnames(AUX,old = "POE",new = "poe[%]")
COLS <- grep(colnames(AUX),pattern="[0123456789]",value=TRUE)
setnames(AUX,old=COLS,new=paste0(COLS," m/s"))

TBL <- AUX |> buildTable(library=LIB, align.body="center",font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER, caption=Caption) 
