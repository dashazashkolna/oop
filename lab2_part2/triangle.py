import turtle
from math import sin, cos, radians

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.position = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)
        self.pivot = (0, 0)

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def set_pivot(self, pivot_x, pivot_y):
        return (pivot_x, pivot_y)

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def centre_bisec(self):
        ab, cb, ac = self.lenghts()
        abc = ab + cb + ac
        x_b = (cb * self.position[0] + ac * self.vertex1[0] + ab * self.vertex2[0]) / abc
        y_b = (cb * self.position[1] + ac * self.vertex1[1] + ab * self.vertex2[1]) / abc
        return (x_b, y_b)

    def centre_median(self):
        x_m = (self.position[0] + self.vertex1[0] + self.vertex2[0]) / 3
        y_m = (self.position[1] + self.vertex1[1] + self.vertex2[1]) / 3

        return (x_m, y_m)

    def lenghts(self):
        ab = ((self.vertex1[0] - self.position[0]) ** 2 + (self.vertex1[1] - self.position[1]) ** 2) ** 0.5
        cb = ((self.vertex1[0] - self.vertex2[0]) ** 2 + (self.vertex1[1] - self.vertex2[1]) ** 2) ** 0.5
        ac = ((self.vertex2[0] - self.position[0]) ** 2 + (self.vertex2[1] - self.position[1]) ** 2) ** 0.5

        return ab, cb, ac

    def rotationVertex(self, coords):
        self.pivot = self.centre_bisec()
        new_x = self.pivot[0] + cos(self.rotation) * (coords[0] - self.pivot[0]) - sin(self.rotation) * (coords[1] - self.pivot[1])
        new_y = self.pivot[1] + sin(self.rotation) * (coords[0] - self.pivot[0]) + cos(self.rotation) * (coords[1] - self.pivot[1])
        return (new_x, new_y)

    def scaleVertex(self, coords):
        new_coords = (coords[0] - self.centre_median()[0], coords[1] - self.centre_median()[1])
        return (self.centre_median()[0] + new_coords[0] * self.scale[0],
                self.centre_median()[1] + new_coords[1] * self.scale[1])

    def draw_rotation(self):
        turtle.up()
        start = Triangle.rotationVertex(self, self.position)
        turtle.setpos(start)
        turtle.down()
        turtle.goto(Triangle.rotationVertex(self, self.vertex1))
        turtle.goto(Triangle.rotationVertex(self, self.vertex2))
        turtle.goto(start)

    def draw_scale(self):
        turtle.up()
        scaledVertex1 = Triangle.scaleVertex(self, self.vertex1)
        scaledVertex2 = Triangle.scaleVertex(self, self.vertex2)
        scaledPos = Triangle.scaleVertex(self, self.position)
        turtle.setpos(scaledPos)
        turtle.down()
        turtle.goto(scaledVertex1)
        turtle.goto(scaledVertex2)
        turtle.goto(scaledPos)


if __name__ == '__main__':
    triangle = Triangle(0, 100, 100, 0)
    turtle.speed(0)
    for degree in range(10, 370, 10):
        turtle.speed(0)
        triangle.set_rotation_degree(degree)
        triangle.draw_rotation()
    turtle.clear()
    for step in range(50):
        triangle.set_scale(step / 5, step / 5)
        triangle.draw_scale()

    turtle.mainloop()