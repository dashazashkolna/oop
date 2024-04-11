from triangle import Triangle
from rectangle import Rectangle
from trapeze import Trapeze
from parallelogram import Parallelogram
from circle import Circle
from ball import Ball
from triangular_pyramid import TriangularPyramid
from quadrangular import QuadrangularPyramid
from parallelepiped import RectangularParallelepiped
from cone import Cone
from prism import TriangularPrism


def maxi(cur_max, check):
    if check[1] > cur_max[1]:
        return check
    return cur_max

result = open('result.txt', 'w')
files = ['input01.txt', 'input02.txt', 'input03.txt']
for file in files:
    cur_max = ['', 0]    # 0 - figure, 1 - volume
    with open(file) as f:
        for line in f:
            data = [el for el in line.split()]
            try:
                if data[0] == 'Triangle':
                    obj = Triangle(int(data[1]), int(data[2]), int(data[3]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Rectangle':
                    obj = Rectangle(int(data[1]), int(data[2]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Trapeze':
                    obj = Trapeze(int(data[1]), int(data[2]), int(data[3]), int(data[4]))
                    if obj._exists():
                        cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Parallelogram':
                    obj = Parallelogram(int(data[1]), int(data[2]), int(data[3]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Circle':
                    obj = Circle(int(data[1]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Ball':
                    obj = Ball(int(data[1]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'TriangularPyramid':
                    obj = TriangularPyramid(int(data[1]), int(data[2]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'QuadrangularPyramid':
                    obj = QuadrangularPyramid(int(data[1]), int(data[2]), int(data[3]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'RectangularParallelepiped':
                    obj = RectangularParallelepiped(int(data[1]), int(data[2]), int(data[3]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'Cone':
                    obj = Cone(int(data[1]), int(data[2]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
                elif data[0] == 'TriangularPrism':
                    obj = TriangularPrism(int(data[1]), int(data[2]), int(data[3]), int(data[4]))
                    cur_max = maxi(cur_max, [str(obj), obj._volume()])
            except AssertionError:
                pass

    result.write(f'Фігура з найбільшою мірою у файлі {file}: {cur_max} \n')
