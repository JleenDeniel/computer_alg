import numpy
from numpy.polynomial.polynomial import polysub, polydiv, polymul


def GCD_rec(first: int, second: int):
    """Recursive  Greatest Common Divisor  for number"""
    if first == 0:
        return second, 0, 1
    d, x1, y1 = gcd_r(second % first, first)
    x = y1 - second // first * x1
    y = x1
    return d, x, y


def GCD(first: int, second: int):
    """Iterative  Greatest Common Divisor for number"""
    x, xt, y, yt = 1, 0, 0, 1
    while second:
        q = first // second
        first, second = second, first % second
        x, xt = xt, x - xt * q
        y, yt = yt, y - yt * q
    return first, x, y


def PolyGCD(a: numpy.array, b: numpy.array):
    """Iterative Greatest Common Divisor  for polynomial"""

    # if len(a) < len(b):
    #     a, b = b, a
    x, xt, y, yt = (1,), (0,), (0,), (1,)
    while any(num != 0.0 for num in b):
        q = polydiv(a, b)[0]
        a, b = b, polydiv(a, b)[1]
        x, xt = xt, polysub(x, polymul(xt, q))
        y, yt = yt, polysub(y, polymul(yt, q))
    return a, x, y


def PolyGCD_rec(a: numpy.array, b: numpy.array):
    """Recursive Greatest Common Divisor  for polynomial"""

    if all(num == 0.0 for num in a):
        return b, 0, 1
    t = polydiv(b, a)
    d, x1, y1 = PolyGCD_rec(t[1], a)
    x = polysub(y1, polymul(t[0], x1))
    y = x1
    return d, x, y


if __name__ == '__main__':
    # a, b = 1234, 33
    # dd, xx, yy = GCD_rec(a, b)
    # print(gcd_r.__doc__)
    # print(f'{a}*{xx} + {b}*{yy} = {dd}', a * xx + b * yy == dd, sep='\n')
    #
    # dd, xx, yy = GCD(a, b)
    # print(gcd_i.__doc__)
    # print(f'{a}*{xx} + {b}*{yy} = {dd}', a * xx + b * yy == dd, sep='\n', end='\n\n')

    # a, b = (-3, 4, 1, 7), (0, 1)
    a, b = (17, 18, 19, 20), (0, 0, 0, 1)
    dd, xx, yy = PolyGCD(a, b)
    # print(gcdp_i.__doc__)
    print(f'{a}*{xx} + {b}*{yy} = {dd}')

    dd, xx, yy = PolyGCD_rec(a, b)
    # print(gcdp_r.__doc__)
    print(f'{a}*{xx} + {b}*{yy} = {dd}')
