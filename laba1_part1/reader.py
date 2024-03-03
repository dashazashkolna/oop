from triangle import Triangle
from rectangle import Rectangle
from circle import Circle
from trapeze import Trapeze
from parallelogram import Parallelogram


names = ['input01.txt', 'input02.txt', 'input03.txt']
for file in names:
    max_area = 0
    max_per = 0
    cur_figure = ''
    with open(file) as f:
        for line in f:
            data = line.split()
            type = data[0]
            if type == "Triangle":
                a, b, c = [int(el) for el in data[1:]]
                figure = Triangle(a, b, c)
                if figure.exist():
                    if figure.area() > max_area:
                        max_area = figure.area()
                        max_per = figure.perimeter()
                        cur_figure = 'Triangle ' + str(a) + ' ' + str(b) + ' ' + str(c)
            elif type == "Rectangle":
                a, b = [int(el) for el in data[1:]]
                figure = Rectangle(a, b)
                if figure.area() > max_area:
                        max_area = figure.area()
                        max_per = figure.perimeter()
                        cur_figure = 'Rectangle ' + str(a) + ' ' + str(b)
            elif type == "Parallelogram":
                a, b, h = [int(el) for el in data[1:]]
                figure = Parallelogram(a, b, h)
                if figure.exist():
                    if figure.area() > max_area:
                        max_area = figure.area()
                        max_per = figure.perimeter()
                        cur_figure = 'Parallelogram ' + str(a) + ' ' + str(b) + ' ' + str(h)
            elif type == "Circle":
                r = int(data[1])
                figure = Circle(r)
                if figure.area() > max_area:
                    max_area = figure.area()
                    max_per = figure.perimeter()
                    cur_figure = 'Circle ' + str(r)
            elif type == "Trapeze":
                a, b, c, d = [int(el) for el in data[1:]]
                figure = Trapeze(a, b, c, d)
                if figure.exist():
                    if figure.area() > max_area:
                        max_area = figure.area()
                        max_per = figure.perimeter()
                        cur_figure = 'Trapeze ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d)

    print('Figure with the max area in the file', file, cur_figure, '\n' 'Area:', max_area, 'Perimeter:', max_per, '\n')