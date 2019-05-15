from sys import argv
if argv[1] == 'tk':
    from tkinterdisplay import TKinterDisplay as Display
else:
    from pygletdisplay import PygletDisplay as Display


d = Display()
d.go()









