shoot = ["mercury", "venus", "earth", "mars", "jupiter", "neptune"]
v = list(shoot) 

v[3] = "pluto"
shoot = tuple(v)
print(shoot)