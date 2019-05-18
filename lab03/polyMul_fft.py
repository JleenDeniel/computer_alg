import numpy as np

from lab03.fft import fft


# def mul(f: np.array, g: np.array):
#     l_f = len(f)
#     l_g = len(g)
#     max_len = l_f + l_g - 1
#
#     if l_f == 0 or l_g == 0:
#         return [0] * (max_len + 1)
#
#     if l_f == 1:
#         return np.dot(g, f[0])
#     if l_g == 1:
#         return np.dot(f, g[0])
#
#     f, g = list(f), list(g)
#     if l_f != l_g:
#         if l_f > l_g:
#             g += [0] * (l_f - l_g)
#         else:
#             f += [0] * (l_g - l_f)
#
#     f += [0]
#     g += [0]
#
#     # max_len = len(f) + len(g) - 1
#     # f = list(f) + [0] * len(f)
#     # g = list(g) + [0] * len(g)
#     # if len(f) != len(g):
#     #     if len(f) > len(g):
#     #         g += [0] * (len(f) - len(g))
#     #     else:
#     #         f += [0] * (len(g) - len(f))
#
#     f = fft(f)
#     g = fft(g)
#
#     c = f * g
#
#     t = fft(c, reverse=True)
#     res = []
#     for i in range(t.shape[0]):
#         res.append(int(t[i].real + 0.5))
#     while res[-1] == 0 and len(res) > max_len:
#         res.pop()
#     return np.dot(res, 1/len(c))


def mul(f: np.array, g: np.array):
    f, g = list(f), list(g)
    if not f:
        raise ValueError("First parameter is empty")
    if not g:
        raise ValueError("Second parameter is empty")
    if any([i is None for i in f]):
        raise ValueError("Array cannot include None")
    if any([i is None for i in g]):
        raise ValueError("Array cannot include None")
    max_len = len(f) + len(g) - 1
    f += [0]*len(f)
    g += [0]*len(g)

    if len(f) > len(g):
        g += [0] * (len(f) - len(g))
    elif len(g) > len(f):
        f += [0] * (len(g) - len(f))

    f = fft(f)
    g = fft(g)

    c = f * g
    # c = np.fft.ifft(c)
    c = fft(c, reverse=True)

    res = [round(x.real) for x in c]

    while res[-1] == 0.0 and len(res) > max_len:
        res.pop()
    return res


# def test(repeats: int = 10):
#     good = []
#     for i in range(repeats):
#         s1 = int(random() * 1000)
#         s2 = int(random() * 1000)
#         a = np.random.randint(0, 100, s1)
#         b = np.random.randint(0, 100, s2)
#
#         r1, r2 = mul(a, b), np.polymul(a, b)
#         try:
#             good.append(np.allclose(r1, r2))
#         except ValueError:
#             print(f'mul() = {r1[:5]} {r1[-5:]} len = {len(r1)}')
#             print(f'polymul() = {r2[:5]} {r2[-5:]} len = {len(r2)}\n\n')
#     print(all(good))


if __name__ == '__main__':
    pass
    # test(10)
    # a = [1, 1, 1]
    # a1 = copy(a)
    # b = [2, 5, 8, 4, 3]
    # # a = np.arange(4)
    # # b = np.arange(4)
    # print('np = ', np.polymul(a, b))
    # print('mul = ', mul(a, b))
    # print(fft(a1))
    # print(np.fft.fft(a1))
