library(sp)
data(meuse)
coordinates(meuse) <- c("x", "y")
plot(meuse)
title("points")
