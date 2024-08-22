library(data.table)
# Functions
.buildA3D <- function(DT=NULL,Rmax=NULL,Mmax=NULL,bins=20){
  on.exit(expr={rm(list = ls())}, add = TRUE)
  stopifnot(!is.null(DT),nrow(DT)>0)
  Mmax <- ifelse(is.null(Mmax),max(DT$Mw),min(max(DT$Mw),Mmax))
  Rmax <- ifelse(is.null(Rmax),max(DT$R),min(max(DT$R),Rmax))
  
  R_GRID <- seq(from=min(DT$R),to=Rmax,length.out=bins)
  # Mw_GRID <- seq(from=min(DT$Mw),to=Mmax,length.out=length(R_GRID))
  Mw_GRID <- seq(from=min(DT$Mw),to=Mmax,length.out=bins)
  DT <- DT[,.(
    R=approx(x=R,y=p,xout=R_GRID,ties = "ordered")$x,
    p=approx(x=R,y=p,xout=R_GRID,ties = "ordered")$y),by=.(Mw)]
  
  DT <- DT[,.(
    Mw=approx(x=Mw,y=p,xout=Mw_GRID,ties = "ordered")$x,
    p=approx(x=Mw,y=p,xout=Mw_GRID,ties = "ordered")$y),by=.(R)]
  
  
  X = DT$R |> unique()#c(1,2,3,4,5)
  Y = DT$Mw |> unique() #c(1,2,3,4,5)
  z <- NULL
  for(x in X){
    for(y in Y){
      z <- c(z,DT[R==x & Mw==y]$p  )
    }
  }
  NR <- length(X)
  NC <- length(Y)
  Z <-  matrix(z, nrow=NR, ncol=NC, byrow=TRUE)
  # get modes
  Mm <- DT$Mw[which.max(DT$p)]
  Rm <-  DT$R[which.max(DT$p)]
  A3D <- list(X=X,Y=Y,Z=Z,Mm=Mm,Rm=Rm)
  return(A3D)
}

# Example
# Read data
RMwTable <- fread("data/RMwTable.csv")

# Select Target
TR_TARGET <- 10000
Tn_TARGET <- 0
POE_TARGET <- (1-exp(-50/TR_TARGET)) |> round(digits=5)

# Set plot parameters
BINS <- 25
R_MAX <- 50
M_MAX <- 7.5
THETA <- -70
PHI <- 20
DT <- RMwTable[Tn==Tn_TARGET & POE==POE_TARGET,.(Mw,R,p)][R<=R_MAX & Mw<=M_MAX] #1-exp(-50/10000)
A3D <- .buildA3D(DT,bins=BINS,Rmax=R_MAX,Mmax=M_MAX)

# ****************************************************
png(filename = "disaggregation_plot.png", width = 1200, height = 800)
# ****************************************************

plot3D::hist3D(
  plot=TRUE,
  x=A3D$X,y=A3D$Y,z=A3D$Z,
  contour = FALSE,
  main = "Dissagregation of Mw and R",
  along="xy",
  theta=-THETA,
  phi=PHI, 
  box=TRUE,
  axes=FALSE,label=FALSE, facets = TRUE,
  nticks=5, 
  xlab = "R [km]", ylab = "Mw", zlab = "POE",
  ticktype="detailed", 
  lighting=list(ambient = 0.8),
  shade=0.75,
  space=0,  
  d = 1
)
# ****************************************************
dev.off()
# ****************************************************
