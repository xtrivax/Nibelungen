init python:
    # Class for Ppaces on the map
    class Place(object):
        def __init__(self, x, y, name, IsActive):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive


    Places = []
    t = 0

    # appends 50 instances to the list Places
    while t < 50:
        Places.append(Place(0,0,"",False))
        t += 1

    # Defines the first 4 Places on the Map an there coordinates
    # For the Map system look also into file scripts/mapscreen.rpy
    Places[0] = Place(730,190, "Arena", True)
    Places[1] = Place(120,250, "Cave", True)
    Places[2] = Place(355,745, "Castle", True)
    Places[3] = Place(1770,275, "City", True)
