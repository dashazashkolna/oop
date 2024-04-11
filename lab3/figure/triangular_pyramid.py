from triangle import Triangle


class TriangularPyramid(Triangle):
    def __init__(self, _a, _h):
        super().__init__(_a, _a, _a)
        self._h = _h

    def _dimension(self):
        return 3

    def _volume(self):
        return 1 / 3 * super()._square() * self._h

    def _square_surface(self):
        apothem = (self._h ** 2 + (self._a / 2) ** 2) ** 0.5
        return 1 / 2 * apothem * 3 * self._a

    def _square_base(self):
        return super()._square()

    def _height(self):
        return self._h

    def __str__(self):
        return f'TriangularPyramid {self._a, self._h}'
