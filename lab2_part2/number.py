import turtle
class Number:
    def __init__(self, way, start):
        self.way = way
        self.start = start

    def draw(self):
        turtle.up()
        turtle.setheading(0)
        turtle.goto(self.start)
        turtle.down()
        for angle in self.way:
            if angle == 'up':
                turtle.up()
                turtle.right(-90)
                turtle.forward(10)
                turtle.down()
            else:
                turtle.right(angle)
                turtle.forward(20)
        turtle.up()
