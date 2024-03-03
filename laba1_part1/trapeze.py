class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    def exist(self):
        p = (self.a + self.c + self.d - self.b) / 2
        sq_triangle = (p * ((p - self.c) * (p - self.d) * (p - self.a + self.b)))
        if sq_triangle > 0:
            return True
        return False

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        return p


    def area(self):
        height = (self.c ** 2 - (((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2)/(2*abs(self.a-self.b))) ** 2) ** 0.5
        s = (self.a + self.b)/2 * height
        return s

if __name__ == '__main__':
    t = Trapeze(8, 0, 4, 5)
    if t.exist():
        print(t.area())