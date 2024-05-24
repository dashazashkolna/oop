from equation import Equation
from quadratic import QuadraticEquation
from biquadratic import BiQuadraticEquation

names = ['input01.txt', 'input02.txt', 'input03.txt']
res = ['result01.txt', 'result02.txt', 'result03.txt']
k = 0

for file in names:
    cur_file = open(res[k], 'w')
    one_solve = dict()
    with open(file) as f:
        for line in f:
            if line.split() != []:
                data = [int(el) for el in line.split()]
                if len(data) == 2:
                    obj = Equation(*data)
                elif len(data) == 3:
                    obj = QuadraticEquation(*data)
                else:
                    obj = BiQuadraticEquation(data[0], data[2], data[4])

                if len(obj.solve()) == 1:
                    one_solve[float(obj.solve()[0])] = str(obj)
                cur_file.write(str(obj) + '\n')
                cur_file.write(str(obj.solve()) + '\n')

    k += 1

    print(f"Рівняння з найменшим розв'язком {file}:", one_solve[min(one_solve)])
    print(f"Рівняння з найбільшим розв'язком {file}:", one_solve[max(one_solve)], '\n')