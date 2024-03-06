id = 1
class Vector:
    def __init__(self, coords):
        global id
        if isinstance(coords, Vector):
            self.coords = coords.coords
        else:
            self.coords = coords
        self.id = id
        id += 1

    def show(self):
        print('Vector', self.id, 'coordinates:', *self.coords)

    def dim(self):
        return len(self.coords)

    def lenght(self):
        under_root = 0
        for i in self.coords:
            under_root += i ** 2
        return under_root ** 0.5

    def average(self):
        return sum(self.coords) / self.lenght()

    def maximin(self):
        return (max(self.coords), min(self.coords))


if __name__ == '__main__':
    vec = Vector([1, 1, 10, 2])
    vec.show()
    vec2 = Vector(vec)
    vec2.show()
    print(vec2.dim())
    print(vec2.lenght())
    print(vec2.average())
    print(*vec2.maximin())