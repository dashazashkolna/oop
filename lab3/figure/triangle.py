from figure import Figure


class Triangle(Figure):
    def __init__(self, _a, _b, _c):
        assert _a + _b > _c and _a + _c > _b and _b + _c > _a
        self._a = _a
        self._b = _b
        self._c = _c

    def _dimension(self):
        return 2

    def _perimetr(self):
        return self._a + self._b + self._c

    def _square(self):
        p = self._perimetr() / 2
        s = (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
        return s

    def __str__(self):
        return f'Triangle {self._a, self._b, self._c}'

if __name__ == '__main__':
    l = str(Triangle(1, 2, 2))
    print(l)