"""
Task 2
"""
from typing import List


def get_common(arr1, arr2) -> List:
    """ Return a list of elements common to <arr1> and <arr2>,
    without repeats. Implemented with O(n) efficiency.

    Precondition:
        - <arr1> and <arr2> are sorted
    """
    common = []
    if len(arr1) == 0 or len(arr2) == 0:
        return common
    i1, i2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] > arr2[i2]:
            i2 += 1
        elif arr2[i2] > arr1[i1]:
            i1 += 1
        else:
            if arr1[i1] not in common:
                common.append(arr1[i1])
            i1 += 1
            i2 += 1
    return common


if __name__ == '__main__':
    print(get_common([1, 2, 3], [2, 3, 4, 5]))


