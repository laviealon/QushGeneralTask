"""
Task 2
"""


def calc_fib_sum(limit):
    first, second, fsum, count = 1, 1, 0, 0
    while count < limit:
        fsum = fsum + first
        third = first + second
        first, second = second, third
        count += 1
    return fsum


if __name__ == '__main__':
    print(calc_fib_sum(100))
