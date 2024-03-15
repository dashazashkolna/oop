import turtle
from number import Number
from math import sin, cos, radians

class Dial:
    def __init__(self):
        self.numbers = {
            0: (0, 90, 0, 90, 90, 0),
            1: (90, 0),
            2: (0, 90, 90, -90, -90),
            3: (0, 90, 90, 180, 90, 90),
            4: (90, -90, -90, 180, 0),
            5: (0, 180, -90, -90, 90, 90),
            6: (0, 180, -90, 0, -90, -90, -90),
            7: (0, 90, 0),
            8: (0, 90, 0, 90, 90, 0, 180, -90),
            9: (0, 90, 90 , 90, 90, 90, 0 , 90),
            10: (90, 0, 'up', 0, -90, 0, -90, -90 , 0),
            11: (90, 0, 'up', -90, 0),
            12: (90, 0, 'up', 0, 180, 90, 90, -90, -90)
        }

        self.position = (0, 270)
        self.rotation = 0
        self.new = (0, 0)

    def set_degree(self, degree):
        self.rotation = radians(degree)

    def point(self):
        new_x = cos(self.rotation) * self.position[0] - sin(self.rotation) * self.position[1]
        new_y = sin(self.rotation) * self.position[0] + cos(self.rotation) * self.position[1]
        self.new = (new_x, new_y)
        return self.new

    @staticmethod
    def draw_circle():
        turtle.up()
        turtle.goto(0, -310)
        turtle.down()
        turtle.circle(310)

    def draw_nums(self, k):
        num = Number(self.numbers[k], (self.new[0]-12, self.new[1]+15))
        num.draw()


if __name__ == '__main__':
    t = Dial()
    t.draw_circle()
    turtle.speed(0)
    k = 0
    hours = [x for x in range(12, 0, -1)]
    for x in range(0, 360, 30):
        t.set_degree(x)
        turtle.up()
        turtle.goto(t.point())
        t.draw_nums(hours[k])
        k += 1
    turtle.mainloop()
