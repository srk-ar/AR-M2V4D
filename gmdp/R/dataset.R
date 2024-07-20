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
  
  
} 


# Fundamental Periods ----
if(REBUILD_MAT){
  MAT <- data.table()
  
  # 
  id <- "Rock impoundment"
  Hs <- 115
  b <- 2840
  s <- 6
  SCN <- data.table(Hs=Hs,Water=0,Clays=0,Sands=0,Gravels=100,Silts=0,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  # 
  id <- "Stock Pile (West)"
  Hs <- 100
  b <- 940
  s <- 6
  SCN <- data.table(Hs=Hs,Water=0,Clays=0,Sands=0,Gravels=100,Silts=0,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  
  id <- "Stock Pile (East)"
  Hs <- 100
  b <- 314
  s <- 6
  SCN <- data.table(Hs=Hs,Water=0,Clays=0,Sands=0,Gravels=100,Silts=0,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  
  id <- "Rock Berm"
  Hs <- 50
  b <- 20
  s <- 2
  SCN <- data.table(Hs=Hs,Water=0,Clays=0,Sands=0,Gravels=100,Silts=0,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  id <- "Sand & Silt impoundment"
  Hs <- 50
  b <- 470
  s <- 3.5
  SCN <- data.table(Hs=Hs,Water=0,Clays=0,Sands=0,Gravels=0,Silts=100,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  
  id <- "Clay impoudment"
  Hs <- 34
  b <- 1000
  s <- 2
  SCN <- data.table(Hs=Hs,Water=0,Clays=100,Sands=0,Gravels=0,Silts=0,POP=0)
  L1 <-  gmdp::fitModel.Shear(level=0.05,.newdata=SCN)
  L2 <-  gmdp::fitModel.Shear(level="mean",.newdata=SCN)
  L3 <-  gmdp::fitModel.Shear(level=0.95,.newdata=SCN)
  L1 <- data.table(Name=id,b=b,s=s,Hs=Hs,L1)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L2 <- data.table(Name=id,b=b,s=s,Hs=Hs,L2)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  L3 <- data.table(Name=id,b=b,s=s,Hs=Hs,L3)[,lo := (b/(2*Hs*s+b)) |> round(digits=3)][]
  MAT <- rbindlist(list(MAT,L1,L2,L3))
  
  
  saveRDS(MAT, "data/MAT.Rds")
  
  #saveRDS(AEPTable, "data/TS.Rds")
}

# Seismic Coefficient ----



