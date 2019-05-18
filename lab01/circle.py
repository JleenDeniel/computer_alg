from lab01.gcd import GCD


def InverseMod(a: int, n: int):
    d, x, y = GCD(a, n)
    if d != 1:
        return None
    else:
        return x % n


if __name__ == '__main__':
    while True:
        n = int(input('Кольцо по модулю вычетов\n'))
        a = int(input('Элемент\n'))
        print(InverseMod(a, n))
