from src.vector2d import Vector2D


class Particle:

    def __init__(self, r, xy, vxy):
        self.r = r
        self._pos = Vector2D(* xy)
        self._vel = Vector2D(*vxy)

    @property
    def x(self): return self._pos.x

    @x.setter
    def x(self, new):   self._pos.x = new

    @property
    def y(self): return self._pos.y

    @y.setter
    def y(self, new):   self._pos.y = new

    @property
    def vx(self): return self._vel.x

    @vx.setter
    def vx(self, new):   self._vel.x = new

    @property
    def vy(self): return self._vel.y

    @vy.setter
    def vy(self, new):   self._vel.y = new

    def move(self, dt):
        self._pos += self._vel * dt

    def bounce(self, bounding_box):
        xmin, xmax, ymin, ymax = bounding_box

        excess = xmin - (self._pos.x - self.r)
        if excess > 0:
            self._pos.x += 2 * excess
            self._vel.x = - self._vel.x

        excess = (self._pos.x + self.r) - xmax
        if excess > 0:
            self._pos.x -= 2 * excess
            self._vel.x = - self._vel.x

        excess = ymin - (self._pos.y - self.r)
        if excess > 0:
            self._pos.y += 2 * excess
            self._vel.y = - self._vel.y

        excess = (self._pos.y + self.r) - ymax
        if excess > 0:
            self._pos.y -= 2 * excess
            self._vel.y = - self._vel.y
