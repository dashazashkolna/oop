import turtle
from random import randint
from math import sin, cos, pi, radians

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.colors = []
        self.rotation = 0
        self.position = (0, 0)
        self.scale = (1, 1)

    def cur_color(self):
        self.colors = []
        with open('colors.txt') as f:
            for line in f:
                for el in line.split():
                    self.colors.append('#' + el)
        k = randint(0, len(self.colors)-1)
        return self.colors[k]

    def cur_position(self):
        self.position = (randint(-300,300), randint(-300, 300))
        return self.position

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rotationMatrix(self):
        fi = self.rotation
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        return fiMatrix

    @staticmethod
    def multMatrixVector(M, v):
        turnedVertex1 = [0, 0]
        turnedVertex1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVertex1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVertex1


    def calc_abs_pos(self):
        M = self.rotationMatrix()
        turnedVertex1 = Triangle.multMatrixVector(M, self.vertex1)
        turnedVertex2 = Triangle.multMatrixVector(M, self.vertex2)

        v1 = (self.position[0] + turnedVertex1[0],
              self.position[1] + turnedVertex1[1])
        v2 = (self.position[0] + turnedVertex2[0],
              self.position[1] + turnedVertex2[1])
        return (v1, v2)

    def draw_random(self):
        turtle.up()
        turtle.color(Triangle.cur_color(self))
        t = Triangle.cur_position(self)
        turtle.setpos(t)
        turtle.down()
        turtle.goto(self.vertex1)
        turtle.goto(self.vertex2)
        turtle.goto(t)

    def draw_rotation(self):
        turtle.up()
        turtle.setpos(0,0)
        turtle.down()
        turtle.goto(Triangle.calc_abs_pos(self)[0])
        turtle.goto(Triangle.calc_abs_pos(self)[1])
        turtle.goto(0,0)



if __name__ == '__main__':
    triangle = Triangle(randint(-200,200), randint(-200,200), randint(-200,200), randint(-200,200))
    #triangle.draw()
    for degree in range(3, 363, 3):
        turtle.speed(50)
        triangle.set_rotation_degree(degree)
        triangle.draw_rotation()

    turtle.mainloop()



