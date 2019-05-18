from typing import Union, Optional
import numpy as np
from numpy.polynomial.polynomial import Polynomial as Poly
from lab01.circle import InverseMod


def rev(p: Poly, n: int) -> Poly:
    p = del_zero(p)
    result = p.coef[::-1]
    if len(p.coef) < n:
        result = np.concatenate([np.zeros(n - len(p.coef)), result])
    return Poly(result)


def del_zero(p: Optional[Poly]) -> Poly:
    return p.trim()
    # count = 0
    # for i in p.coef[::-1]:
    #     if abs(i) < 10 ** -5:
    #         count += 1
    #     else:
    #         break
    # return p.truncate(len(p.coef) - count) if len(p.coef) != count else Poly([0])


def PolyInverseModOverQ(f: Poly, mod_deg: int) -> Union[Poly, None]:
    if mod_deg < 1:
        raise ValueError('Не допустимое значение модуля')
    if f.coef[0] == 0:
        return None

    g = Poly([1 / f.coef[0]])
    r = int(np.ceil(np.log2(mod_deg)))
    d = 2
    for i in range(r):
        g = (2 * g - f * g ** 2).truncate(d)
        d <<= 1
    return g


def PolyInverseModOverZn(f: Poly, mod_deg: int, mod_ring: int) -> Union[Poly, None]:
    if mod_deg < 1 or mod_ring < 1:
        raise ValueError('Модуль не может быть меньше 1')

    if f.coef[0] == 0 or mod_ring == 1:
        return None

    # f.coef = np.array([int(i % mod_ring) for i in f.coef], int)
    f = Poly(np.mod(f.coef, mod_ring))

    c = InverseMod(f.coef[0], mod_ring)
    if c is None:
        return None

    g = Poly([c])
    r = int(np.ceil(np.log2(mod_deg)))
    d = 2

    for i in range(r):
        g = (2 * g - f * g ** 2).truncate(d)
        g = Poly(np.mod(g.coef, mod_ring))
        d <<= 1
    return g


def PolyDivModOverQ(a: Poly, b: Poly) -> (Poly, Poly):
    if not b.coef.any():
        raise ZeroDivisionError

    a = del_zero(a)

    b = del_zero(b)
    n, m = len(a.coef), len(b.coef)

    if n < m:
        return Poly([0]), a
    else:
        f = rev(b, m)
        g = PolyInverseModOverQ(f, n - m + 1)
        q = (rev(a, n) * g).truncate(n - m + 1)
        q = rev(q, n - m + 1)

        if len(q.coef) < n - m + 1:
            q.coef = np.concatenate([np.zeros(n - len(q)), q.coef])

        r = a - b * q
        r = del_zero(r)
        q = del_zero(q)
        return q, r


def PolyDivModOverZn(a: Poly, b: Poly, mod_r: int) -> (Poly, Poly):
    if mod_r < 1:
        raise ValueError

    if mod_r == 1:
        raise ZeroDivisionError

    a = Poly(np.mod(a.coef, mod_r))
    b = Poly(np.mod(b.coef, mod_r))

    a = del_zero(a)

    # deleted_zero = 0
    # for i in b.coef[::-1]:
    #     if abs(i) < 10 ** -10:
    #         deleted_zero += 1
    #     else:
    #         break

    b = del_zero(b)
    n, m = len(a.coef), len(b.coef)

    if n < m:
        return Poly([0]), a
    else:
        f = rev(b, m) # - deleted_zero)
        g = PolyInverseModOverZn(f, n - m + 1, mod_r)

        if g is None:
            raise ZeroDivisionError

        q = (rev(a, n) * g).truncate(n - m + 1)
        q = Poly(np.mod(q.coef, mod_r))
        q = rev(q, n - m)

        if len(q.coef) < n - m + 1:
            q.coef = np.concatenate([np.zeros(n - m + 1 - len(q)), q.coef])

        bq = Poly(np.mod((b * q).coef, mod_r))
        r = a - bq
        r = Poly(np.mod(r.coef, mod_r))
        q = Poly(np.mod(q.coef, mod_r))
        r = del_zero(r)
        q = del_zero(q)
        return q, r
