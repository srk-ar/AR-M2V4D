source("R/setup.R")
# uhs ----
if(REBUILD_UHS){
  # 
  UHSTable <- data.table()
  AEPTable <- data.table()
  
  
  Vs30_TARGET <- c(220,580,760,910,1500)
  
  for(Vs in Vs30_TARGET){
    GMDP <- buildGMDP(vref=Vs,path=paste0("../oq/output/nrc/",Vs,"/"),IDo="nrc_v3.19.1")
    UHSTable <- rbind(UHSTable,GMDP$UHSTable)
    AEPTable <- rbind(AEPTable,GMDP$AEPTable)
  }
  
  saveRDS(UHSTable, "data/UHSTable.Rds")
  saveRDS(AEPTable, "data/AEPTable.Rds")
} else {
  UHSTable <- readRDS("data/UHSTable.Rds")
  AEPTable <- readRDS("data/AEPTable.Rds")

}


# Fundamental Periods ----
if(REBUILD_TS){
 
  NR_TARGET <- 100
  LEVELS <- c(0.05,0.10,0.16,0.50,"mean",0.84,0.90,0.95)
  SHT <- data.table()
  MAT <- data.table(
    ID=c("RI","SPW","SPE","RB","SSI","CI","TMF"),
    Name=c("Rock impoundment","Stock Pile (West)","Stock Pile (East)","Rock Berm","Sand & Silt impoundment","Clay impoudment","Tailings Management Facility"),
    b=c(2840,940,314,20,470,1000,15),
    s=c(6,6,6,2,3.5,2,12),
    Hs=c(115,100,100,50,50,34,35)
  )
  # MAT[,lo:=(b/(2*Hs*s+b)) |> round(digits=3)]
  MAT <- MAT[,.(ID,Name,b,s,lo=(b/(2*Hs*s+b)) |> round(digits=3)),by=.(ID,Name,b,s,Hs)]
  
  # "Rock impoundment"
  AUX <- MAT[ID=="RI",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("GW","GM","ML"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  
  # 
  AUX <- MAT[ID=="SPW",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("GP","GM","ML","SM"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  
  # 
  AUX <- MAT[ID=="SPE",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("GW","GP","GM","SP"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)

  # 
  AUX <- MAT[ID=="RB",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("GW","GP","GM"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  # 
  AUX <- MAT[ID=="SSI",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("ML","SM"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  # 
  AUX <- MAT[ID=="CI",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("CL","ML","SC","SM"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  
  AUX <- MAT[ID=="TMF",.(ID,Name,b,s,lo,getSiteProperties(Hs=Hs,USCS=c("GW","GM","ML"),NR=NR_TARGET,levels=LEVELS))]
  SHT <- rbind(SHT,AUX)
  
  
  # Fundamental periods ----
  SHT[, an := mapply(function(mo, lo) {
    getCylinderRoots(mo = mo, lo = lo, no = 1, model = "nlm", extrapolate = TRUE)|> round(4) |> suppressWarnings()
  }, mo, lo)]
  
  
  SHT[,Ts:=(4*pi*Hs/(an*(2 - mo)*VSo)) |> round(3)]
  saveRDS(MAT, "data/MAT.Rds")
  saveRDS(SHT, "data/SHT.Rds")
  
} else {
  SHT <- readRDS("data/SHT.Rds")
  MAT <- readRDS("data/MAT.Rds")
}



# Seismic Coefficient ----


if(REBUILD_KIT){
  TR_TARGET <- c(475,975,2475,5000,10000)
  Vs30_TARGET <- c(220,580,760,910,1500)
  p_TARGET <- c(0.50,"mean",0.84,0.90,0.95)
  SHT <- readRDS("data/SHT.Rds")
  SHT <- SHT[level %in% p_TARGET,.(ID,Name,Hs=Hs,Tso=Ts,p=level)]
  
  UHS <- UHSTable[SM=="openquake" & Vs30 %in% Vs30_TARGET    & TR %in% TR_TARGET & p%in% p_TARGET]
  DnTable <-  UHS[,dsra::fitModel.Dn.TR(Sa=Sa,PGA=PGA,Tn=Tn,Mw = 7.3, xD = 1.3, kymin = 0.001, kymax = 0.55, n = 100), by = .(Tn, TR,Vs30, p)] |> unique()
  DnTRmodel <- DnTable[, .(Tn, TR, p, Ts, Vs30, a, b, e, PGA)] |> unique()
  KhTRmodel <- DnTRmodel[, fitModel.Kmax.TR( a=a,b=b,e=e,pga=PGA,Ts=Ts, n = 100), by = .(Tn, TR, p,Vs30)]
  
  # 
  KIT <- data.table()
  
  
  ID_TARGET <- "RI"
  # Vs30_TARGET <- 360
  # sprintf("Building Seismic coefficients for %s for Vs30=%d m/s\n", ID_TARGET,Vs30_TARGET) |> cat()
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  ID_TARGET <- "SPW"
  # Vs30_TARGET <- 360
  # sprintf("Building Seismic coefficients for %s for Vs30=%d m/s\n", ID_TARGET,Vs30_TARGET) |> cat()
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  ID_TARGET <- "SPE"
  # Vs30_TARGET <- 360
  # sprintf("Building Seismic coefficients for %s for Vs30=%d m/s\n", ID_TARGET,Vs30_TARGET) |> cat()
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  ID_TARGET <- "RB"
  
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  ID_TARGET <- "SSI"
 
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  
  ID_TARGET <- "CI"
  
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  ID_TARGET <- "TMF"
  
  Hs <- SHT[ID==ID_TARGET]$Hs |> unique() 
  Da_TARGET <- Hs*100*XDa
  DATA <- KhTRmodel[SHT[ID==ID_TARGET], on=c("p")] 
  AUX <- DATA[Vs30%in%Vs30_TARGET,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  
  
  KIT <- KIT[,-c("Tso")]
  saveRDS(KIT, "data/KIT.Rds")
} else {
  KIT <- readRDS("data/KIT.Rds")
}

# 
# saveRDS(DnTRmodel, "data/DnTRmodel.Rds")
# saveRDS(KhTRmodel, "data/KhTRmodel.Rds")
