import turtle
from random import randint
from triangle import Triangle

for x in range(100):
    turtle.speed(10)
    t = Triangle(randint(-300, 300), randint(-300, 300), randint(-300, 300), randint(-300, 300))
    t.draw_random()


turtle.mainloop()