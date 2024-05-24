from circle import Circle


class Cone(Circle):
    def __init__(self, _r, _h):
        super().__init__(_r)
        self._h = _h

    def _dimension(self):
        return 3

    def _height(self):
        return self._h

    def _square_base(self):
        return super()._square()

    def _square_surface(self):
        apothem = (self._r ** 2 + self._h ** 2) ** 0.5
        return 3.1415926535 * self._r * apothem

    def _volume(self):
        return 1 / 3 * self._r ** 2 * 3.1415926535 * self._h

    def __str__(self):
        return f'Cone {self._r, self._h}'
    