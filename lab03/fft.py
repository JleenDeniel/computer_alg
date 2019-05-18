from time import time
import pytest
import numpy as np


def dft(x: np.array, reverse: bool = False) -> np.array:
    """
    Iterative DFT algorithm
    This algorithm work only with array which len less or equal 32
    """
    # x = np.asarray(x, dtype=complex)
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    roots = np.exp(2j * np.pi * k * n / N if reverse else -2j * np.pi * k * n / N)
    return np.dot(roots, x) if not reverse else np.dot(roots, x) / N


def dft_over_zn(x: np.array, reverse: bool = False) -> np.array:
    pass


def fft(x: np.array, reverse=False) -> np.array:
    """
    Recursive FFT algorithm
    This FFT algorithm can work only with arrays with len equal power of 2
    Another array will be resize to power of 2
    """
    if any([i is None for i in x]):
        raise ValueError("Array cannot include None")

    if len(x) == 0:
        raise ValueError("Empty array")
    if len(x) == 1:
        return x

    x = np.asarray(x, dtype=complex)
    N = len(x)

    if N <= 32:
        return dft(x, reverse)

    if np.log2(N) % 1 > 0:
        N = 2 ** int(np.ceil(np.log2(N)))
        # x = np.array([0]*(N - x.shape[0]) + list(x))
        x.resize(N, refcheck=False)

    x_even = fft(x[::2], reverse)
    x_odd = fft(x[1::2], reverse)

    roots = np.exp(-2j * np.pi * np.arange(N) / N) if not reverse else np.exp(2j * np.pi * np.arange(N) / N)
    res = np.concatenate([x_even + roots[:N // 2] * x_odd,
                          x_even + roots[N // 2:] * x_odd])
    if reverse:
        res /= 2
    return res


def fft_over_zn(x: np.array, reversed: bool = False) -> np.array:
    pass


if __name__ == '__main__':
    pass
