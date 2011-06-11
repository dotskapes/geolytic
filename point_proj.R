map = user_param ('mapkey', 'Map', 'point_map')
header = user_param ('titlekey', 'Title', 'text')

plot(map, pch=1)
crs_map <- proj4string(map)
title(crs_map)