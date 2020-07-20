planet_list = ["Mercury", "Mars"]
farthest_planets = ['Neptune', 'Pluto']

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(farthest_planets)
planet_list.insert(0, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[-1]