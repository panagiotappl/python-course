from math import cos, sin, pi
from sys import argv
import tkinter as tk

from pyglet import window

from particle import Particle
import pyglet

twopi = 2 * pi


class PygletDisplay:
    def __init__(self):
        self._window = pyglet.window.Window(600, 400)
        self._fps_display = pyglet.clock.ClockDisplay()
        self._fps = 60
        self._p = Particle(30, (self._window.width / 2, self._window.height / 2), (80.0, 150.0))

        self._window.event(self.on_draw)

    @property
    def bounding_box(self):
        return 0, self._window.width, 0, self._window.height

    def update(self, dt):
        self._p.move(dt)
        self._p.bounce(self.bounding_box)

    def on_draw(self):
        self._window.clear()
        p = self._p

        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))
        self._fps_display.draw()

    def go(self):
        pyglet.clock.schedule_interval(self.update, 1 / self._fps)
        pyglet.app.run()


class TKinterDisplay:

    def __init__(self):
        master = tk.Tk()
        canvas = tk.Canvas(master, width=600, height=400, bg='black')
        canvas.pack()
        self._canvas = canvas
        self._p = Particle(30, (canvas.winfo_height() / 2, canvas.winfo_width() / 2), (80.0, 150.0))
        self._fps = 60

    @property
    def bounding_box(self):
        return 0, self._canvas.winfo_width(), 0, self._canvas.winfo_height()

    def draw(self):
        r, x, y, canvas = self._p.r, self._p.x, self._p.y, self._canvas
        canvas.create_oval(x-r, y+r, x+r, y-r, outline="yellow")

    def update(self, dt):
        p, canvas = self._p, self._canvas

        canvas.delete(tk.ALL)
        p.move(dt)
        p.bounce(self.bounding_box)
        self.draw()

        canvas.update()
        canvas.after(17, self.update, 1 / self._fps)

    def go(self):
        self.update(0)
        tk.mainloop()


if argv[1] == 'tk':
    t = TKinterDisplay()
    t.go()
else:
    t = PygletDisplay()
    t.go()



