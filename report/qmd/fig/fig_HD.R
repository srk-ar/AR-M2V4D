# Caption <- CAP  |> sprintf(min(TR_TARGET),max(TR_TARGET),Vs30_TARGET,p_TARGET)
# Caption <- ""
RMwTable <- fread("data/RMwTable.csv")
TR_TARGET <- 10000
Tn_TARGET <- 0
POE_TARGET <- (1-exp(-50/TR_TARGET)) |> round(digits=5)
BINS <- 25
R_MAX <- 50
M_MAX <- 7.5
DT <- RMwTable[Tn==Tn_TARGET & POE==POE_TARGET,.(Mw,R,p)][R<=50 & Mw<=7.5] #1-exp(-50/10000)
A3D <- .buildA3D(DT,bins=BINS,Rmax=R_MAX,Mmax=M_MAX)

plot3D::hist3D(
  plot=TRUE,
  x=A3D$X,y=A3D$Y,z=A3D$Z,
  contour = FALSE,
  main = "Dissagregation of Mw and R",
  along="xy",
  theta=-30,
  phi=70, 
  box=TRUE,
  axes=TRUE,label=TRUE, facets = TRUE,
  nticks=5, 
  xlab = "R [km]", ylab = "Mw", zlab = "POE",
  ticktype="detailed", 
  lighting=list(ambient = 0.8),
  shade=0.75,
  space=0,  
  d = 1
)

# Heat map 2D
# plot3D::image2D(
#   z=A3D$Z,  
#   y=A3D$Y,
#   x=A3D$X,
#   xlab = "R", 
#   ylab = "Mw")



