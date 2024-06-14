from rational import Rational
from iterator import Iterator


class RationalList:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if type(other) == RationalList:
            for x in list(other.array):
                self.array.append(Rational(x)())

        else:
            self.array.append(other())

        return RationalList(self.array)

    def __setitem__(self, index, value):
        self.array[index] = value()

    def __getitem__(self, item):
        return self.array[item]

    def __len__(self):
        return len(self.array)

    def __dict__(self):
        new_dict = {}
        for x in range(len(self.array)):
            new_dict[Rational(self.array[x])['n']] = Rational(self.array[x])['d']

        return new_dict

    def __sort__(self):
        pass

    def __iter__(self):
        return Iterator(self.array)

    def __str__(self):
        return f'{self.array}'


if __name__ == '__main__':
    print(RationalList([]) + RationalList([1, 2, '3/4']) + Rational(4))
    a = RationalList([1,2,3])
    a[0] = Rational(2)
    print(a)
    print(RationalList([1,2])[1])
    b = RationalList([1,2,3]).__dict__()
    print(b)
    print(sorted(b))
    for x in RationalList([1,2,3]):
        print(x)


