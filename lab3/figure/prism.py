from triangle import Triangle


class TriangularPrism(Triangle):
    def __init__(self, _a, _b, _c, _h):
        super().__init__(_a, _b, _c)
        self._h = _h

    def _dimension(self):
        return 3

    def _height(self):
        return self._h

    def _square_base(self):
        return super()._square()

    def _square_surface(self):
        return super()._perimetr() * self._h

    def _volume(self):
        return super()._square() * self._h

    def __str__(self):
        return f'TriangularPrism {self._a, self._b, self._c, self._h}'
