from collections.abc import Callable
import sys
sys.setrecursionlimit(20000)


def partitionLo(A: list[int], lo: int, hi: int) -> int:
    pivot = A[lo]  # choose pivot
    i = lo + 1     # start pointer

    for j in range(lo + 1, hi):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    i -= 1  # get last element less than pivot
    A[lo], A[i] = A[i], A[lo]  # swap pivot to correct location
    return i  # return pivot index


# Sorts a (portion of an) array, divides it into partitions, then sorts those
def quickselect(A: list[int], size: int, index: int,
                partition: Callable[[list[int], int, int], int]) -> int:
    if size == 1:
        return A[0]

    # Partition array and get the pivot index
    pivot = partition(A, 0, size)

    if pivot == index:
        return A[pivot]
    elif pivot > index:
        # Element is to the left of pivot
        return quickselect(A[:pivot], pivot, index, partition)
    else:  # index > pivot
        # Element is to the right of pivot
        return quickselect(A[pivot + 1:], size - pivot - 1,
                           index - pivot - 1, partition)


def QuickSelect(arr, index):
    return quickselect(arr, len(arr), index, partitionLo)
