from dial import Dial
from hand import Hand
import turtle

clock = Dial()
clock.draw_circle()
turtle.speed(0)
k = 0
hours = [x for x in range(12, 0, -1)]
for x in range(0, 360, 30):
    clock.set_degree(x)
    turtle.up()
    turtle.goto(clock.point())
    clock.draw_nums(hours[k])
    k += 1

Hand(10).draw()
turtle.mainloop()