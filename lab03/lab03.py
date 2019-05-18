import numpy as np


def primitive_root(modulo: int, deg: int = None) -> (list, int):
    res = []
    if deg is None:
        deg = modulo - 1
    for i in range(2, modulo):
        if i**deg % modulo == 1:
            res.append(i)
            # tmp = sorted([i ** j % modulo for j in range(1, modulo)])
            # if tmp == list(range(1, modulo)):
            #     res.append(i)
    return res, deg


print(primitive_root(29, 4))
