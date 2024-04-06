from quadratic import QuadraticEquation
class BiQuadraticEquation(QuadraticEquation):
    def __str__(self):
        return f'{self.a}x^4 + {self.b}x^2 + {self.c} = 0'

    def solve(self):
        solutions = set()
        quadratic_sol = super().solve()

        if quadratic_sol == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        for solution in quadratic_sol:
            if solution >= 0:
                t1 = solution ** 0.5
                t2 = -t1
                solutions.add(t1)
                solutions.add(t2)
        return tuple(solutions)


if __name__ == '__main__':
    eq = BiQuadraticEquation(4, -2, -2)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 5, 4)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 4)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 0)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 5, 0)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(1, 3, 8)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(1, 4, 4)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(1, -3, 2)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(2, -6, 4)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(1, 0, 0)
    print(eq)
    print(eq.solve())

