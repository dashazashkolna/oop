class Equation:
    INF = 'infinity'
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.b}x + {self.c} = 0'

    def show(self):
        print(self)

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.INF
            else:
                return ()
        else:
            return (-self.c / self.b,)


if __name__ == '__main__':
    eq = Equation(2, 4)
    eq.show()
    print(eq.solve())

    eq = Equation(0, 4)
    print(eq)
    print(eq.solve())

    eq = Equation(0, 0)
    print(eq)
    print(eq.solve())

    eq = Equation(5, 0)
    print(eq)
    print(eq.solve())