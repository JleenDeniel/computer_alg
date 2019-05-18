from math import *
import numpy as np
from sympy import *

x, y, z = symbols('x,y,z')

# def IntKaratsuba(x,y):
#     if len(str(x)) == 1 or len(str(y)) == 1:
#         return x*y
#     else:
#         m = max(len(str(x)),len(str(y)))
#         m2 = m // 2
#
#         a = x // 10**(m2)
#         b = x % 10**(m2)
#         c = y // 10**(m2)
#         d = y % 10**(m2)
#
#         z0 = IntKaratsuba(b,d)
#         z1 = IntKaratsuba((a+b),(c+d))
#         z2 = IntKaratsuba(a,c)
#
#         return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

def IntKaratsuba(a, b):
    if x < 10 or y < 10:
        return x * y
    m = max(int(log10(x) + 1), int(log10(y) + 1))
    if m % 2 != 0:  # если нечетные
        m -= 1
    m_2 = int(m / 2)
    a, b = divmod(x, 10 ** m_2)
    c, d = divmod(y, 10 ** m_2)
    ac = IntKaratsuba(a, c)
    bd = IntKaratsuba(b, d)
    ad_bc = IntKaratsuba((a + b), (c + d)) - ac - bd
    return (ac * (10 ** m)) + bd + (ad_bc * (10 ** m_2))


def PolyKaratsuba(a, b):
    if len(a) == 1 and len(b) == 1:
        return a * b

    deg_a, deg_b = len(a), len(b)
    if deg_a < deg_b:
        a, b = b, a
        deg_a, deg_b = deg_b, deg_a

    if deg_a & 1:
        deg_a += 1
        a = np.concatenate([np.zeros(1), a])

    if deg_a != deg_b:
        b = np.concatenate([np.zeros(deg_a - deg_b), b])

    a1 = a[:deg_a // 2]
    b1 = b[:deg_a // 2]
    a2 = a[deg_a // 2:]
    b2 = b[deg_a // 2:]

    result_1 = PolyKaratsuba(a1, b1) #f
    result_2 = PolyKaratsuba(a2, b2) #s
    result_3 = PolyKaratsuba(np.polyadd(a1,a2), np.polyadd(b1,b2)) #m
    result_3 = np.polysub(np.polysub(result_3, result_2), result_1)

    result_1 = np.concatenate([result_1, np.zeros(deg_a)])
    result_3 = np.concatenate([result_3, np.zeros(deg_a//2)])

    # return np.polyadd(result_1, np.polyadd(result_2, result_3))
    res = np.polyadd(result_1, np.polyadd(result_2, result_3))
    res = np.polymul(res, [1])
    return res


# g, f = np.array([1, 4, 8]), np.array([1, 2, 3])
# print(PolyKaratsuba(g, f))

def BinPowMod (a, p, n): #a^p=modn
    m = a
    t = 1
    if n==0:
        raise ValueError
    if a==0 and p==0:
        return None
    if a==0:
        return 0
    while p:
     if p & 1:
         t *= m
         t %= n
     m *= m
     p >>= 1
    return t

# print(BinPowMod(0,0,10))
# result_1, result_2, result_3 = np.array([]), np.array([]), np.array([])

# print(karatsuba(int(123), int(456)))
