from vector2d import Vector2D


class Particle:

    def __init__(self, r, pos, vel):
        self.p = Vector2D(*pos)
        self.v = Vector2D(*vel)
        self.r = r

    @property
    def x(self):
        return self.p.x

    @x.setter
    def x(self, new):
        self.p.x = new

    @property
    def y(self):
        return self.p.y

    @y.setter
    def y(self, new):
        self.p.y = new

    @property
    def vx(self):
        return self.v.x

    @vx.setter
    def vx(self, new):
        self.p.x = new

    @property
    def vy(self):
        return self.v.y

    @vy.setter
    def vy(self, new):
        self.v.y = new

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce(self, mm):
        x_min, x_max, y_min, y_max = mm

        excess = x_min - (self.x - self.r)
        if excess > 0:
            self.x += 2 * excess
            self.vx = - self.vx

        excess = (self.x + self.r) - x_max
        if excess > 0:
            self.x -= 2 * excess
            self.vx = - self.vx

        excess = y_min - (self.y - self.r)
        if excess > 0:
            self.y += 2 * excess
            self.vy = - self.vy

        excess = (self.y + self.r) - y_max
        if excess > 0:
            self.y -= 2 * excess
            self.vy = - self.vy
