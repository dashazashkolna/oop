from rational import Rational
from rational_list import RationalList


res = open('result5_3_2.txt', 'w')
files = ['input01.txt', 'input02.txt', 'input03.txt']
for file in files:
    with open(file) as f:
        array = RationalList([])
        new = []
        for line in f:
            if line.split() != []:
                data = [el for el in line.split()]
                for num in data:
                    if '/' in num:
                        new = array + Rational(num)
                    else:
                        new = array + Rational(int(num))
        res.write(f'{sum(new)} \n')
