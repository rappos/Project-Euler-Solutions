"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divisible_by(number, max_divisor):
    for i in range(1, max_divisor + 1):
        if number % i != 0:
            return False
    return True


def main():
    number = 1
    max_divisor = 20
    while True:
        if is_divisible_by(number, max_divisor):
            print(number)
            break
        number += 1


if __name__ == '__main__':
    main()
