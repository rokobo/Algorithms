from random import randint
from Algorithms_Specialization.Quicksort import quicksort, partitionHi, partitionLo, partitionMedianThree


def test_lo_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, 10, partitionLo)
        assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), (test, arr)


def test_hi_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, len(arr), partitionHi)
        assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), (test, arr)


def test_median_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, 10, partitionMedianThree)
        assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), (test, arr)


def test_lo_largeArray() -> None:
    with open('tests/RandomNumbers.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    assert (arr[i] <= arr[i+1] for i in range(len(arr)-1))


def test_hi_largeArray() -> None:
    with open('tests/RandomNumbers.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    assert (arr[i] <= arr[i+1] for i in range(len(arr)-1))


def test_median_largeArray() -> None:
    with open('tests/RandomNumbers.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    assert (arr[i] <= arr[i+1] for i in range(len(arr)-1))
