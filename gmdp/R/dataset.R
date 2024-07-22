source("R/setup.R")
# uhs ----
if(REBUILD_UHS){
  # 
  UHSTable <- data.table()
  AEPTable <- data.table()
  Vs30_TARGET <- c(140,180,250,300,360,450,580,760,910,1100,1500,1600,2000,3000)
  
  for(Vs in Vs30_TARGET){
    GMDP <- buildGMDP(vref=Vs,path=paste0("../oq/output/gem/",Vs,"/"),IDo="gem_v3.19.1")
    UHSTable <- rbind(UHSTable,GMDP$UHSTable)
    AEPTable <- rbind(AEPTable,GMDP$AEPTable)
  }
  AUX <- sapply(c("A","B","BC", "C", "CD", "D", "DE", "E"), SIDtoVs30) |> unname()
  
  Vs30_TARGET <- c(AUX,Vs30_TARGET,220) |> unique() |> sort()
  GMDP <- buildGMDP(vref=760,vs30=Vs30_TARGET,path="../oq/output/gem/760/",IDo="gem_v3.19.1")
  UHSTable <- rbind(UHSTable,GMDP$UHSTable)
  AEPTable <- rbind(AEPTable,GMDP$AEPTable)

  GMDP <- buildGMDP(vref=3000,vs30=Vs30_TARGET,path="../oq/output/gem/3000/",IDo="gem_v3.19.1")
  UHSTable <- rbind(UHSTable,GMDP$UHSTable)
  AEPTable <- rbind(AEPTable,GMDP$AEPTable)
  
  
  Vs30_TARGET <- c(140,180,220,250,300,360,450,580,760,910,1100,1500,1600,2000,3000)
  for(Vs in Vs30_TARGET){
    GMDP <- buildGMDP(vref=Vs,path=paste0("../oq/output/nrc/",Vs,"/"),IDo="nrc_v3.19.1")
    UHSTable <- rbind(UHSTable,GMDP$UHSTable)
    AEPTable <- rbind(AEPTable,GMDP$AEPTable)
  }
  AUX <- sapply(c("A","B","BC", "C", "CD", "D", "DE", "E"), SIDtoVs30) |> unname()
  
  Vs30_TARGET <- c(AUX,Vs30_TARGET,220) |> unique() |> sort()
  GMDP <- buildGMDP(vref=760,vs30=Vs30_TARGET,path="../oq/output/nrc/760/",IDo="nrc_v3.19.1")
  UHSTable <- rbind(UHSTable,GMDP$UHSTable)
  AEPTable <- rbind(AEPTable,GMDP$AEPTable)
  
  GMDP <- buildGMDP(vref=3000,vs30=Vs30_TARGET,path="../oq/output/nrc/3000/",IDo="nrc_v3.19.1")
  UHSTable <- rbind(UHSTable,GMDP$UHSTable)
  AEPTable <- rbind(AEPTable,GMDP$AEPTable)
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
    ID=c("RI","SPW","SPE","RB","SSI","CI"),
    Name=c("Rock impoundment","Stock Pile (West)","Stock Pile (East)","Rock Berm","Sand & Silt impoundment","Clay impoudment"),
    b=c(2840,940,314,20,470,1000),
    s=c(6,6,6,2,3.5,2),
    lo=c(0.05,0.05,0.05,0.05,0.05,0.05),
    Hs=c(115,100,100,50,50,34)
  )
  saveRDS(MAT, "data/MAT.Rds")
  
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
  
  
  # Fundamental periods ----
  SHT[, an := mapply(function(mo, lo) {
    getCylinderRoots(mo = mo, lo = lo, no = 1, model = "nlm", extrapolate = TRUE)|> round(4) |> suppressWarnings()
  }, mo, lo)]
  
  
  SHT[,Ts:=(4*pi*Hs/(an*(2 - mo)*VSo)) |> round(3)]
  saveRDS(SHT, "data/SHT.Rds")
  
} else {
  SHT <- readRDS("data/SHT.Rds")
  MAT <- readRDS("data/MAT.Rds")
}



# Seismic Coefficient ----
if(REBUILD_KIT){
  TR_TARGET <- c(475,1000,2475,5000,10000)
  Vs30_TARGET <- 250# c(250,1100)
  
  Da_TARGET <- c(1,2.5,5,10,15,25)
  p_TARGET <- c(0.05,"mean",0.95)

  
  
  #
  
  SHT <- readRDS("data/SHT.Rds")
  SHT <- SHT[level %in% p_TARGET,.(ID,Name,Tso=Ts,p=level)]
  
  UHS <- UHSTable[Vs30 %in% Vs30_TARGET & SM=="openquake" & ID=="nrc_v3.19.1" & TR %in% TR_TARGET & p%in% p_TARGET][,-c("ID","SM")] #Remove ID column to avoid conflicts with SHT
  
  DnTable <-  UHS[,dsra::fitModel.Dn.TR(Sa=Sa,PGA=PGA,Tn=Tn,Mw = 6.5, xD = 1.3, kymin = 0.001, kymax = 0.55, n = 100), by = .(Tn, TR,Vref,Vs30, p)] |> unique()
  DnTRmodel <- DnTable[, .(Tn, TR, p, Ts, Vs30, Vref, a, b, e, PGA)] |> unique()
  KhTRmodel <- DnTRmodel[, fitModel.Kmax.TR( a=a,b=b,e=e,pga=PGA,Ts=Ts, n = 100), by = .(Tn, TR, p,Vs30,Vref)]
  
  
  KIT <- data.table()
  
  
  # RI
  ID_TARGET <- "RI"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  
  # SPW
  ID_TARGET <- "SPW"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  
  # SPE
  ID_TARGET <- "SPE"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  # RB
  ID_TARGET <- "RB"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  # SSI
  ID_TARGET <- "SSI"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  
  # CI
  ID_TARGET <- "CI"
  sprintf("Building Seismic coefficients for %s", ID_TARGET) |> cat()
  AUX <- KhTRmodel[SHT[ID==ID_TARGET], on="p"][,fitModel.Kmax.Ts(.SD,Tso=Tso,Dao=Da_TARGET,model="rf"),by=.(ID,Name,TR,p,Vs30,Vref,Tso)]
  KIT <- rbindlist(list(KIT,AUX),use.names = TRUE)
  
  KIT <- KIT[,-c("Tso","Vref")]
  saveRDS(KIT, "data/KIT.Rds")
} else {
  KIT <- readRDS("data/KIT.Rds")
}

# 
# saveRDS(DnTRmodel, "data/DnTRmodel.Rds")
# saveRDS(KhTRmodel, "data/KhTRmodel.Rds")
