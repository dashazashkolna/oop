class Triangle:
    def __init__(self, a,  b, c):
        self.a = a
        self.b = b
        self.c = c


    def exist(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        return False


    def perimeter(self):
        p = self.a + self.b + self.c
        return p


    def area(self):
        p = Triangle.perimeter(self)/2
        s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return s


if __name__ == '__main__':
    t = Triangle(12, 4, 10)
    if t.exist():
        print(t.area())