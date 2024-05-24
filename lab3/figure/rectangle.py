from figure import Figure


class Rectangle(Figure):
    def __init__(self, _a, _b):
        self._a = _a
        self._b = _b

    def _dimension(self):
        return 2

    def _perimetr(self):
        return 2 * (self._a + self._b)

    def _square(self):
        return self._a * self._b

    def __str__(self):
        return f'Rectangle {self._a, self._b}'
