REBUILD <- FALSE
source("R/setup.R")
source("R/global.R")
if(REBUILD){
  source("R/dataset.R")
} else {
  UHSTable <- readRDS("data/UHSTable.Rds")
  AEPTable <- readRDS("data/AEPTable.Rds")
}
p_TARGET <- AEPTable$p |> unique()
TR_max <- 100000
Tn_TARGET <- c(0,0.1,0.5,1.0)
DATA <- AEPTable[Vref==1500  & Vs30==1500 & p %in% p_TARGET & Tn==0 ,.(ID=SM,X=Sa,Y=AEP)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=2.0,
  xAxis.log = TRUE,
  yAxis.log = TRUE,
  yAxis.legend="AEP [1/yr]",
  xAxis.legend="Sa [g]",
  group.legend="quantile",
  plot.save=FALSE,
  data=DATA) 
PLOT
buildPlot::export(.x=PLOT, filename=file.path(imagesFolder,"AEP.png"),factor_height=0.5)


#
TR_TARGET <- c(475,1000,2475,5000,10000)
DATA <- UHSTable[Vs30==760 & p =="mean"  & SM=="gmdp" & TR %in% TR_TARGET,.(ID=TR,X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="line",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=2.0,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT



DATA <- UHSTable[Vref==760 & Vs30==760 & SM=="openquake" & TR == 10000,.(ID=p,X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=2.0,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT


DATA <- UHSTable[ Vref==Vs30 & p=="mean" & TR ==2500,.(ID=Vref,X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=2.0,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT

DATA <- UHSTable[ Vs30==220 & p=="mean" & TR ==10000 & SM=="openquake" & ID=="nrc_v3.19.1",.(ID=as.factor(Vref),X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="line",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=0.5,
  point.style=21,
  point.size=2,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT


# Quiero registros del modelo de Diana (ID==nrc_nrc_v3.19.1) para Vs30=760 y p=mean

DATA=UHSTable[ Vs30==220 & p=="mean" & SM=="openquake" & ID=="nrc_v3.19.1" & TR==2475,.(ID=as.factor(Vref),X=Tn,Y=Sa)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="line",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=0.5,
  point.style=21,
  point.size=2,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT



DATA=UHSTable[ Vs30==180 & p==0.50 & SM=="openquake"  & TR==2475,.(ID=ID,X=Tn,Y=Sa)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=1,
  point.style=21,
  point.size=2,
  xAxis.log = TRUE,
  yAxis.log = TRUE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT


DATA=UHSTable[ Vs30==760 & p=="mean" & SM=="openquake" & ID=="nrc_v3.19.1" & TR %in% c(475,1000,2475,5000,10000),.(ID=TR,X=Tn,Y=Sa)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "hc",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=1,
  point.style=21,
  point.size=2,
  xAxis.log = FALSE,
  yAxis.log = FALSE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT

