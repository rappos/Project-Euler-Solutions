from math import sqrt, ceil


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    summa = 0
    for i in range(2_000_000):
        if is_prime(i):
            summa += i
    print(summa)


if __name__ == '__main__':
    main()
