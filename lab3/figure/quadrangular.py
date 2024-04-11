from rectangle import Rectangle


class QuadrangularPyramid(Rectangle):
    def __init__(self, _a, _b, _h):
        super().__init__(_a, _b)
        self._h = _h

    def _dimension(self):
        return 3

    def _square_base(self):
        return super()._square()

    def _square_surface(self):
        new_a = self._a * (((self._a / 2) ** 2 + self._h ** 2) ** 0.5)
        new_b = self._b * (((self._b / 2) ** 2 + self._h ** 2) ** 0.5)
        return new_a + new_b

    def _height(self):
        return self._h

    def _volume(self):
        return 1 / 3 * super()._square() * self._h

    def __str__(self):
        return f'QuadrangularPyramid {self._a, self._b, self._h}'
