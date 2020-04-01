# using Mapscreen and define the coordinates to the same size as the background ("map.jpg")
screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpg"

        # loops trough Places list and checks wheter is it active or not.
        # if it is active the button will be set.
        for q in Places:
            if q.IsActive:
                button:
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name)
