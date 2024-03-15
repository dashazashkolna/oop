from datetime import datetime
from math import radians, cos, sin
import turtle
import time

class Hand:
    def __init__(self, t):
        self.time = int(datetime.now().strftime("%S"))
        self.t = t

    def start_pos(self):
        degree = radians(6) * self.time
        return degree

    def point(self):
        new_x = sin(self.start_pos()) * 200
        new_y = cos(self.start_pos()) * 200
        return new_x, new_y

    def draw(self):
        turtle.speed(0)
        fixed_time = time.time()
        while time.time() - fixed_time < self.t:
            turtle.color('black')
            turtle.goto(Hand(self).point())
            turtle.down()
            turtle.color('white')
            turtle.goto(0, 0)



if __name__ == '__main__':
    Hand(10).draw()
    turtle.mainloop()