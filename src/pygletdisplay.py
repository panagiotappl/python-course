from math import pi, cos, sin

import pygletdisplay

from particle import Particle
twopi = 2 * pi


class PygletDisplay:
    def __init__(self):
        self._window = pygletdisplay.window.Window(600, 400)
        self._fps_display = pygletdisplay.clock.ClockDisplay()
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

        pygletdisplay.gl.glColor3f(1.0, 1.0, 0)
        pygletdisplay.graphics.draw(20, pygletdisplay.gl.GL_LINE_LOOP,
                                    ('v2f', tuple(circle_vertices())))
        self._fps_display.draw()

    def go(self):
        pygletdisplay.clock.schedule_interval(self.update, 1 / self._fps)
        pygletdisplay.app.run()
