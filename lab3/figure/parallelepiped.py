from rectangle import Rectangle


class RectangularParallelepiped(Rectangle):
    def __init__(self, _a, _b, _c):
        super().__init__(_a, _b)
        self._c = _c

    def _dimension(self):
        return 3

    def _height(self):
        return self._c

    def _square_base(self):
        return super()._square()

    def _square_surface(self):
        new_a = 2 * self._a * self._c
        new_b = 2 * self._b * self._c
        return new_a + new_b

    def _volume(self):
        return self._a * self._b * self._c

    def __str__(self):
        return f'RectangularParallelepiped {self._a, self._b, self._c}'
