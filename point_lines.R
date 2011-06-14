map = user_param ('mapkey', 'Map', 'point_map')
header = user_param ('titlekey', 'Title', 'text')

plot(map)
crs_map <- proj4string(map)
title(crs_map)

cc <- coordinates(map)
m.sl <- SpatialLines(list(Lines(list(Line(cc)), "1")))
plot(m.sl, add=TRUE)