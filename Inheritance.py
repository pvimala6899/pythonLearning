class office:
    def __init__(own, name,role):
        own.Name = name
        own.Role =role

    def employee(own):
        print("your name is " + own.Name + own.Role)

ofc = employee(office):
  pass
ofc=employee("vimal", "analyst")        
ofc.employee()