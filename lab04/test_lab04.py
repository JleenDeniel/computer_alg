from numpy.polynomial.polynomial import polydiv, Polynomial as Poly
from lab04 import poly_div
from random import randint
import pytest
import numpy as np

a = [np.random.randint(100, size=randint(1, 20)) for i in range(100)]
b = [np.random.randint(100, size=randint(1, 10)) for i in range(100)]

param = [(a[i], b[i]) for i in range(len(a))]


# @pytest.mark.skip
@pytest.mark.parametrize("f, g", param)
def test_poly_div_quotient(f, g):
    res = poly_div(Poly(f), Poly(g))[0].coef
    res_np = list(polydiv(f, g)[0])
    print(res)
    print(res_np)
    assert np.allclose(res, res_np)
