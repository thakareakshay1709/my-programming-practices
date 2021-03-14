from fractions import Fraction
from functools import reduce


def product(fracs):
    # print(fracs)
    t = reduce(lambda num, den: num * den, fracs)  # complete this line with a reduce statement
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
