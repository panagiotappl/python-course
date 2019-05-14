from math import sqrt


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        if key == 1:
            self.y = value

    def __add__(self, vector):
        return Vector2D(self.x + vector[0], self.y + vector[1])

    def __sub__(self, vector):
        return Vector2D(self.x - vector[0], self.y - vector[1])

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, s):
        return Vector2D(self.x * s, self.y * s)

    def __rmul__(self, s):
        return Vector2D(self.x * s, self.y * s)

    def __truediv__(self, s):
        return Vector2D(self.x / s, self.y / s)

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

