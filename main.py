from gl import Render

r = Render(800, 600)

r.glClearColor(0,0,0)
r.glClear()
r.glColor(0,0,1)
points = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
r.paint(points)
points = [(321, 335), (288, 286), (339, 251), (374, 302)]
r.paint(points)
points = [(277, 149), (311, 97), (336, 149)]
r.paint(points)
points = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
(597, 215), (552, 214), (517, 144), (466, 180)]
r.paint(points)

points = [(682, 175), (708, 120), (735, 148), (739, 170)]
r.paint(points)
#r.load('Yoshi.obj',(20,10),(75,75))
r.glFinish()