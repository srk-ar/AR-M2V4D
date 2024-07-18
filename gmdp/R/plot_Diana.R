UHSTable <- readRDS("data/UHSTable.Rds")


# Ejemplo Eliminar Stewart
UHSTable <- UHSTable[SM!="gmdp",-c("SM","AF","sdLnAF","Vref")]

# Ejemplo: Eliminar GEM
# UHSTable <- UHSTable[ID!="gem_v3.19.1",-c("ID")]


library(data.table)
fwrite(UHSTable,"UHS.csv")

# Install devtools if you haven't already
install.packages("devtools")

# Install buildPlot from GitHub
devtools::install_github("averriK/buildPlot")
library(buildPlot)


p_TARGET <- AEPTable$p |> unique()
TR_max <- 100000
Tn_TARGET <- c(0,0.1,0.5,1.0)
DATA <- AEPTable[Vref==1500  & Vs30==1500 & p %in% p_TARGET & Tn==0 ,.(ID=SM,X=Sa,Y=AEP)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "highcharter",
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


# Stewart (SM=='gmdp") con Vref=760 y Vs30=220, valor medio, para TR=475,1000,2475,5000,10000
TR_TARGET <- c(475,1000,2475,5000,10000)
DATA <- UHSTable[Vref==760 & Vs30==220 & p =="mean"  & SM=="gmdp" & TR %in% TR_TARGET,.(ID=TR,X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "highcharter",
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


# Stewart (SM=='gmdp") versus NRC (SM=='openquake") ID=="nrc_v3.19.1" con Vref=760 y Vs30=220, valor medio, para TR=10000
TR_TARGET <- c(475,1000,2475,5000,10000)
DATA <- UHSTable[Vref==760 & Vs30==760 & p =="mean"   & TR == 2475,.(ID=ID,X=Tn,Y=Sa)][order(X)]|> unique()

PLOT <- buildPlot(
  library = "highcharter",
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
  library = "highcharter",
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
  library = "highcharter",
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
  library = "highcharter",
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
  library = "highcharter",
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

# fwrite(DATA,"myEcel.csv")
# writexl::write_xlsx(DATA,"myExcel.xlsx")

DATA=UHSTable[ Vs30==180 & p==0.50 & SM=="openquake"  & TR==2475,.(ID=ID,X=Tn,Y=Sa)][order(X)]|> unique()
PLOT <- buildPlot(
  library = "highcharter",
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
  library = "highcharter",
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


# Quiero registros del modelo de Diana (ID==nrc_nrc_v3.19.1) para Vs30=760 y p=mean

UHS_data <- UHSTable[Vref==760 & Vs30==760 &p=="mean" & SM=="openquake" & ID=="nrc_v3.19.1" & TR==2475,.(ID=as.factor(Vref),X=Tn,Y=Sa)][order(X)]|> unique()

NRC_760 <- data.table(ID="NRC 760 2475", X=c(0.01,0.2,0.5,1,2,5,10), Y=c(.107,.209,.0953,.0449,.0195,.00471,.00171))

DATA <- rbindlist(list(UHS_data,NRC_760))

PLOT <- buildPlot(
  library = "highcharter",
  xAxis.label =TRUE,
  yAxis.label =TRUE,
  plot.type="spline",
  legend.layout="vertical",
  legend.show=TRUE,
  line.size=1,
  point.style=21,
  point.size=2,
  xAxis.log = FALSE,
  yAxis.log = TRUE,
  xAxis.legend="Tn [s]",
  yAxis.legend="Sa [g]",
  group.legend="TR [yr]",
  plot.save=FALSE,
  data=DATA) 
PLOT
