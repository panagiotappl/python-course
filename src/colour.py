class Colour:
    @classmethod
    def from_rgb_01(cls, r, g, b):
        return cls(r, g, b)

    @classmethod
    def from_rgb_f(cls, rgb):
        return cls(*(cls.f_to_n[d] / 15.0 for d in rgb.lower()))

    def __init__(self, r, g, b):
        self._rgb_01 = (r, g, b)

    def as_rgb_01(self):
        return self._rgb_01

    f_to_n = {d: n for n, d in enumerate('0123456789abcdef')}
    n_to_f = {n: d for d, n in f_to_n.items()}

    def as_rgb_f(self):
        return ''.join(self.n_to_f[int(v*15)] for v in self._rgb_01)

    def __hash__(self):
        return hash(self._rgb_01)

    def __eq__(self, other):
        return hasattr(other, '_rgb_01') and self._rgb_01 == other._rgb_01

    def __str__(self):
        return f'<{self.__class__.__name__}: {str(self._rgb_01)}>'

    def __repr__(self):
        return f'{self.__class__.__name__}{str(self._rgb_01)}' # Colour(0,0,0)


Color = Colour

Colour.BLACK = Colour.from_rgb_01(0, 0, 0)
Colour.WHITE = Colour.from_rgb_01(1, 1, 1)
Colour.RED = Colour.from_rgb_01(1, 0, 0)
Colour.GREEN = Colour.from_rgb_01(0, 1, 0)
Colour.BLUE = Colour.from_rgb_01(0, 0, 1)
Colour.YELLOW = Colour.from_rgb_01(1, 1, 0)
Colour.CYAN = Colour.from_rgb_01(0, 1, 1)
Colour.MAGENTA = Color.from_rgb_01(1, 0, 1)
