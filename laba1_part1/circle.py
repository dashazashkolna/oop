class Circle:
    def __init__(self, r):
        self.r = r


    def perimeter(self):
        l = 2 * 3.14 * self.r
        return l


    def area(self):
        s = 3.1415926535 * (self.r ** 2)
        return s


if __name__ == '__main__':
    c = Circle(8)
    print(c.area())