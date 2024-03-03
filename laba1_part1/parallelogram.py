class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h


    def exist(self):
        if (self.a > self.h or self.b > self.h) and self.a * self.b * self.h != 0:
            return True
        return False


    def perimeter(self):
        return 2 * (self.a + self.b)


    def area(self):
        if self.b < self.h:
            return self.h * self.b
        else:
            return self.h * self.a


if __name__ == '__main__':
    p = Parallelogram(12, 4, 24)
    if p.exist():
        print(p.area())
