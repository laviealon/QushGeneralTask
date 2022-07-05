"""
Task 4
"""


def digit_adder(digit: int) -> int:
    sum1 = digit + int(str(digit) + str(digit))
    sum2 = int(str(digit) + str(digit) + str(digit)) + int(str(digit) + str(digit) + str(digit) + str(digit))
    return sum1 + sum2
