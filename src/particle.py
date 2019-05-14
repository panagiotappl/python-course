class Particle:

    def __init__(self, r, xy, vxy):
        self.x, self.y = xy
        self.vx, self.vy = vxy
        self.r = r

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
