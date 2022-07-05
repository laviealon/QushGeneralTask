"""
Task 3
"""


def contains_odd(n: int) -> bool:
    s = str(n)
    for char in s:
        if int(char) % 2 == 1:
            return False
    return True
