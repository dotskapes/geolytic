map = user_param ('mapkey', 'Map', 'point_map')
x = user_param ('xkey', 'X Field', 'attr', 'mapkey')
y = user_param ('ykey', 'Y Field', 'attr', 'mapkey')

plot (map[[x]], map[[y]])