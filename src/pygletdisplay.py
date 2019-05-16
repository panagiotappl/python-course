from math import pi, cos, sin
import pyglet

from display import Display

twopi = 2 * pi


class PygletDisplay(Display):
    def __init__(self):
        self._window = pyglet.window.Window(600, 400)
        self._fps_display = pyglet.clock.ClockDisplay()
        self._fps = 60
        self._particles = []

        self._window.event(self.on_draw)

    @property
    def bounding_box(self):
        return 0, self._window.width, 0, self._window.height

    def update(self, dt):
        particles = self._particles
        for particle in particles:
            particle.move(dt)
            particle.bounce(self.bounding_box)

    def on_draw(self):
        particles = self._particles

        self._window.clear()
        for particle in particles:

            def circle_vertices():
                delta_angle = twopi / 20
                angle = 0
                while angle < twopi:
                    yield particle.x + particle.r * cos(angle)
                    yield particle.y + particle.r * sin(angle)
                    angle += delta_angle

            x, y, z = particle.colour.as_rgb_01()
            pyglet.gl.glColor3f(x, y, z)
            pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                                        ('v2f', tuple(circle_vertices())))
            self._fps_display.draw()

    def go(self):
        pyglet.clock.schedule_interval(self.update, 1 / self._fps)
        pyglet.app.run()
