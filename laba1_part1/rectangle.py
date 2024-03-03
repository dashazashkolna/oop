class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def perimeter(self):
        p = 2 * (self.a + self.b)
        return p


    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    r = Rectangle(7, 2)
    print(r.area())
