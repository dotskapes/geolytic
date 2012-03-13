map = user_param ('mapkey', 'Map', 'point_map')

cuts=c(0,20,50,200,500,2000)
grys <- grey.colors(7, 0.90, 0.50, 2.2)
print(spplot(map[7:14], main = "precip", cuts=cuts, cex=.5, col.regions=grys),split=c(1,1,2,1),more=T)