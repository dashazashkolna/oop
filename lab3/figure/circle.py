from figure import Figure


class Circle(Figure):
    def __init__(self, _r):
        self._r = _r

    def _dimension(self):
        return 2

    def _perimetr(self):
        assert self._dimension() == 2
        return 2 * 3.1415926535 * self._r

    def _square(self):
        return 3.1415926535 * self._r ** 2

    def __str__(self):
        return f'Circle {self._r}'
