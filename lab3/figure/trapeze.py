from figure import Figure


class Trapeze(Figure):
    def __init__(self, _a, _b, _c, _d):
        self._a = _a
        self._b = _b
        self._c = _c
        self._d = _d

    def _dimension(self):
        return 2

    def _perimetr(self):
        return self._a + self._b + self._c + self._d

    def _square(self):
        height = (self._c ** 2 -
                  (((self._a - self._b) ** 2 + self._c ** 2 - self._d ** 2) /
                   (2 * abs(self._a - self._b))) ** 2) ** 0.5

        s = (self._a + self._b) / 2 * height
        return s

    def _exists(self):
        p = (self._a + self._c + self._d - self._b) / 2
        sq_triangle = (p * ((p - self._c) * (p - self._d) * (p - self._a + self._b)))
        if sq_triangle > 0:
            return True
        return False

    def __str__(self):
        return f'Trapeze {self._a, self._b, self._c, self._d}'
