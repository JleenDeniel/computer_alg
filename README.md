# computer_alg
Computer algebra labs

## lab01 Done
### Задание 1
Реализация алгоритма Евклида в итеративной и рекурсивной формах
```
from numpy.polynomial.polynomial import Polynomial as Poly

def GCD(a : int, b : int) −> (int, int, int):
...
def GCD_rec(a : int, b : int) −> (int, int, int):
...
def PolyGCD(a : Poly, b : Poly) −> (Poly, Poly, Poly):
...
def PolyGCD_rec(a : Poly, b : Poly) −> (Poly, Poly, Poly):
...
```
### Залание 2
Нахождение обратного по модулю элемента в кольце по модулю вычетов при помощи алгоритма Евклида
```
a^−1 mod n
def InverseMod(a : int, n : int) −> int:
...
```

## lab02 Done
### Задание 1
Алгоритм Евклида перемножения целых чисел и многочленов
```
import numpy as np

def IntKaratsuba(a : int, b : int) −> int:
...
def PolyKaratsuba(a : np.array, b : np.array) −> np.array:
...
```
### Задание 2
Бинарное взведение в степень по модулю
```
a^p mod n
def BinPowMod(a : int, p : int, n : int) −> int:
...
```

## lab03

Not done

## lab04 Done
### Задание 1
Обратный полиом по модулю при помощи метода Ньютона

`f * g =  1 mod x^r`
```
from numpy.polynomial.polynomial import Polynomial as Poly

def PolyInverseModOverQ(f : Poly, r : int) −> Poly:
...
def PolyInverseModOverZn(f : Poly, r : int, n : int) −> Poly:
...
```
### Задание 2
Функции деления двух полином с остатком для рациональных полиномов и полиномов с коеффициентами в кольце по модулю
```
from numpy.polynomial.polynomial import Polynomial as Poly

def PolyDivModOverQ(a, b : Poly) −> (Poly, Poly):
...
def PolyDivModOverZn(a, b : Poly, n : int) −> (Poly, Poly):
...
```
