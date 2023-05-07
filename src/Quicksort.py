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


def partitionHi(A: list[int], lo: int, hi: int) -> int:
    # set last element as first element to act as pivot
    A[lo], A[hi - 1] = A[hi - 1], A[lo]
    return partitionLo(A, lo, hi)


def partitionMedianThree(A: list[int], lo: int, hi: int) -> int:
    # selects median value between first, last and middle elements
    median = (lo + hi) // 2  # middle value is temporarily set as median
    first, middle, last = A[lo], A[median], A[hi - 1]

    if first < middle:
        if middle < last:
            pass
        elif first < last:
            median = hi - 1
        else:
            median = lo
    else:
        if first < last:
            median = lo
        elif middle < last:
            median = hi - 1

    # set median element as first element to act as pivot
    A[lo], A[median] = A[median], A[lo]
    return partitionLo(A, lo, hi)


# Sorts a (portion of an) array, divides it into partitions, then sorts those
def quicksort(A: list[int], lo: int, hi: int,
              partition: Callable[[list[int], int, int], int]) -> None:
    if lo >= hi:
        return

    # Partition array and get the pivot index
    pivot = partition(A, lo, hi)

    # Sort the two partitions (left and right side of pivot)
    quicksort(A, lo, pivot, partition)
    quicksort(A, pivot + 1, hi, partition)
    return


def QuickSort(arr):
    quicksort(arr, 0, len(arr), partitionMedianThree)
    return
