source("R/setup.R")

if(REBUILD){
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

