import numpy as np


def binary_pow(a, deg: int, t = int):
    res = 1
    while deg:
        if deg & 1:
            res *= a
        a *= a
        deg >>= 1
    return t(res)


def binary_pow_mod(a: int, deg: int, n: int):
    res = 1
    if a == 0:
        if p != 0:
            return 0
        else:
            return None
    if p < 0 or n <= 1:
        return 0
    while deg:
        if deg & 1:
            res *= a
        a *= a
        res %= n
        a %= n
        deg >>= 1
    return res


def binary_matrix(a: np.array, deg: int):
    res = np.identity(len(a))
    while deg:
        if deg & 1:
            res = np.dot(res, a)
        a = np.dot(a, a)
        deg >>= 1
    return res


def fib(n):
    arr = np.array([[1, 1], [1, 0]], dtype='O')
    return int(binary_matrix(arr, n)[1, 0])


print(fib(9))
print(ffib(9))
