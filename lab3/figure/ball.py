from circle import Circle


class Ball(Circle):
    def _dimension(self):
        return 3

    def _square(self):
        return None

    def _square_surface(self):
        return super()._square() * 4

    def _height(self):
        return self._r * 2

    def _volume(self):
        return 4 / 3 * 3.1415926535 * self._r ** 3

    def __str__(self):
        return f'Ball {self._r}'


if __name__ == '__main__':
    print(Ball(4)._perimetr())
