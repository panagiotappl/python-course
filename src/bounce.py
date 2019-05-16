from sys import argv

from colour import Colour
from particle import Particle

if argv[1] == 'tk':
    from tkinterdisplay import TKinterDisplay as Display
else:
    from pygletdisplay import PygletDisplay as Display


d = Display()
d.add(Particle(30, (600 / 2, 400 / 2), (80.0, 150.0), Colour.RED))
d.add(Particle(45, (600 / 2, 400 / 2), (100.0, 60.0), Colour.MAGENTA))
d.add(Particle(10, (600 / 2, 400 / 2), (70.0, 20.0), Colour.CYAN))
d.add(Particle(20, (600 / 2, 400 / 2), (100.0, 20.0), Colour.GREEN))

d.go()









