class Figure:
    def _dimension(self):
        return None

    def _perimetr(self):
        assert self._dimension() == 2
        return None

    def _square(self):
        assert self._dimension() == 2
        return None

    def _square_surface(self):
        assert self._dimension() == 3
        return None

    def _square_base(self):
        assert self._dimension() == 3
        return None

    def _height(self):
        assert self._dimension() == 3
        return None

    def _volume(self):
        if self._dimension() == 2:
            return self._square()
        return None
