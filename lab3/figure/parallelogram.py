from figure import Figure


class Parallelogram(Figure):
    def __init__(self, _a, _b, _h):
        self._a = _a
        self._b = _b
        self._h = _h

    def _dimension(self):
        return 2

    def _perimeter(self):
        return 2 * (self._a + self._b)

    def _square(self):
        if self._b < self._h:
            return self._h * self._b
        else:
            return self._h * self._a

    def __str__(self):
        return f'Parallelogram {self._a, self._b, self._h}'
