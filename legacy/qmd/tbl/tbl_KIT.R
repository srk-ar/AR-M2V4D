Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
# Name <- SHT[ID==ID_TARGET]$Name |> unique()
Da_TARGET <- Hs*100*XDa
Ts_TARGET <- SHT[ID==ID_TARGET & level==p_TARGET]$Ts |> unique() 
Caption <- CAP |> sprintf(TR_TARGET,Vs30_TARGET,Ts_TARGET,min(Da_TARGET),100*min(XDa),max(Da_TARGET),100*max(XDa),p_TARGET)
AUX <- KIT[ ID==ID_TARGET & TR==TR_TARGET & Vs30==Vs30_TARGET & p==p_TARGET][,-c("Name")]


TBL <- AUX |> buildTable(library=LIB,font.size.body = FONT.SIZE.BODY,font.size.header = FONT.SIZE.HEADER,font.bold.header=TRUE, caption=Caption)
