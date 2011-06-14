map = user_param ('mapkey', 'Map', 'point_map')
header = user_param ('titlekey', 'Title', 'text')
y = user_param ('ykey', 'Y Field', 'attr', 'mapkey')

def.par <- par(no.readonly = TRUE)
par(mar=c(0.1,0.1,2,0.1))

plot(map, pch = 1, cex = sqrt(map[[y]]/20))

legVals <- c(50, 100, 200)
legend("left", legend=legVals, pch = 1, pt.cex = sqrt(legVals)/20, bty = "n",
 title="measured, ppt", cex=0.8, y.inter=0.9)

title(header)

par(def.par)