library(gmdp)
library(dsra)
library(buildPlot)
library(buildTable)
library(data.table)
library(grid)
library(png)
library(knitr)


.buildFigure <- function(PLOT,DELAY=0.3,imagesFolder="_var",params=list(background="white")){
  FILE <- tempfile(tmpdir = imagesFolder,pattern="fig",fileext=".png")
  XDELAY <- max(DELAY,round(nrow(DT)/1500*DELAY,digits = 2))
  AUX <- tempfile(pattern="fig",fileext=".html")
  htmlwidgets::saveWidget(widget = PLOT,background=params$background, file = AUX,selfcontained = TRUE)
  webshot2::webshot(delay=XDELAY,url = AUX, file = FILE)
  FIG <- knitr::include_graphics(path=FILE)
  return(FIG)
}

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
