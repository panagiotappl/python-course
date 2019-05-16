from math import sqrt
from operator import add, neg, eq, sub


def Vector(names):

    class Vector:

        def __init__(self, *args):
            if len(args) != len(names):
                raise TypeError
            self._values = list(args)

        def __getitem__(self, key):
            return self._values[key]

        def __setitem__(self, key, value):
            self._values[key] = value

        def __repr__(self):
            return f'{Vector.__name__}{tuple(self._values)}'

        def __eq__(self, other):
            return all(map(eq, self, other))

        def __neg__(self):
            return Vector(*map(neg, self))

        def __add__(self, other):
            return Vector(*map(add, self, other))

        def __sub__(self, other):
            return Vector(*map(sub, self, other))

        def __mul__(self, n):
            return Vector(*(x*n for x in self))

        def __div__(self, n):
            return Vector(*(x/n for x in self))

        def __abs__(self):
            return sqrt( sum(x*x for x in self))

        __rmul__ = __mul__
        __truediv__ = __div__

    for i, name in enumerate(names):
        setattr(Vector, name, make_property(i))

    Vector.__name__ = f'Vector({repr(names)})'

    return Vector


def make_property(n):
    def get(self):
        return self._values[n]

    def set(self, v):
        self._values[n] = v
    return property(get, set)


Vector2D = Vector('xy')
Vector3D = Vector('xyz')
