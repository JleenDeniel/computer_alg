import numpy as np
import pytest
import random

from lab03.fft import fft
from lab03.polyMul_fft import mul

# for fft test
size_arr = [i for i in range(10, 100)]

# for polynomial multiply test
size_multiply = [(random.randint(1, 100), random.randint(1, 100)) for i in range(100)]


# @pytest.mark.skip("Test random FFT skipped")
@pytest.mark.parametrize("size", size_arr)
def test_fft_random(size: int):
    """
    This FFT algorithm can work only with arrays with len equal power of 2
    """
    a = np.random.randint(-1000, 1000, size)
    a_len = a.shape[0]

    if np.log2(a_len) % 1 > 0:
        a_len = 2 ** int(np.ceil(np.log2(a_len)))
        a.resize(a_len, refcheck=False)

    f = fft(a)
    assert np.allclose(f, np.fft.fft(a)), f'fft {f}\nnp.fft {np.fft.fft(a)}'


# @pytest.mark.skip("Test random inverse FFT skipped")
@pytest.mark.parametrize("size", size_arr)
def test_fft_inv_random(size: int):
    """
    This FFT algorithm can work only with arrays with len equal power of 2
    """
    a = np.random.randint(-1000, 1000, size)
    a_len = a.shape[0]

    if np.log2(a_len) % 1 > 0:
        # print("This FFT algorithm can work only with arrays with len equal power of 2")
        a_len = 2 ** int(np.ceil(np.log2(a_len)))
        a.resize(a_len, refcheck=False)

    f = fft(a, True)

    assert np.allclose(f, np.fft.ifft(a)), f'fft {f}\nnp.fft {np.fft.ifft(a)}'


# @pytest.mark.skip("Test random multiply with FFT skipped ")
@pytest.mark.parametrize("size_a, size_b", size_multiply)
def test_mul_random(size_a: int, size_b: int):
    a = np.random.randint(-1000, 1000, size_a)
    b = np.random.randint(-1000, 1000, size_b)

    # print()
    # print('a = ', a)
    # print('b = ', b)

    res_mul = mul(a, b)
    res_np = list(np.polymul(a, b))

    assert res_mul == res_np, f'mul = {res_mul}\nres_np = {res_np}'

    # print(res_mul)


param = [
    ([], [3, 5]),
    ([5, 8, 0, 3], []),
    ([6], [5, 7, None, 0, 7]),
    ([6, 3, None, 1], [7])
]


# @pytest.mark.skip("Test multiply for sample")
@pytest.mark.parametrize("a, b", param)
def test_mul_err_sample(a, b):
    with pytest.raises(ValueError):
        mul(a, b)


a = [
    np.array([1, 0, 0]),
    np.array([0, 0, 1]),
    np.array([3]),
    [7],
    np.array([1, 0, 4, 7, 2]),
    np.array([i for i in range(64, 0, -1)])
]
b = [np.fft.fft(i) for i in a]
param = [(a[i], b[i]) for i in range(len(a))]


# @pytest.mark.skip("Test FFT with samples skipped")
@pytest.mark.parametrize("sample, equal", param)
def test_fft_sample(sample, equal):
    assert np.allclose(fft(sample), equal)


b = [np.fft.ifft(i) for i in a]
param = [(a[i], b[i]) for i in range(len(a))]


# @pytest.mark.skip("Test inverse FFT with samples skipped")
@pytest.mark.parametrize("sample, equal", param)
def test_fft_inv_sample(sample, equal):
    assert np.allclose(fft(sample, reverse=True), equal)


param = [
    np.array([None, 2, 5]),
    np.array([1, 2, 3, None, 2, 5]),
    np.array([None]),
    np.array([]),
    [],
]


# @pytest.mark.skip("Test FFT for ValueError")
@pytest.mark.parametrize("sample", param)
def test_fft_error(sample):
    with pytest.raises(ValueError):
        fft(sample)


# @pytest.mark.skip("Test inverse FFT for ValueError")
@pytest.mark.parametrize("sample", param)
def test_fft_rev_error(sample):
    with pytest.raises(ValueError):
        fft(sample, reverse=True)
