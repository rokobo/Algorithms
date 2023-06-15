from random import randint
from Quicksort import quicksort, partitionHi, partitionLo, partitionMedianThree


def test_lo_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, 10, partitionLo)
        assert arr == sorted(arr), (test, arr)


def test_hi_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, len(arr), partitionHi)
        assert arr == sorted(arr), (test, arr)


def test_median_pivot() -> None:
    for test in range(30):
        arr = [randint(0, 100) for _ in range(10)]
        quicksort(arr, 0, 10, partitionMedianThree)
        assert arr == sorted(arr), (test, arr)


def test_lo_large_array() -> None:
    with open('tests/LargeArrayQuicksort.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    quicksort(arr, 0, len(arr), partitionLo)
    assert arr == sorted(arr)


def test_hi_large_array() -> None:
    with open('tests/LargeArrayQuicksort.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    quicksort(arr, 0, len(arr), partitionHi)
    assert arr == sorted(arr)


def test_median_large_array() -> None:
    with open('tests/LargeArrayQuicksort.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    quicksort(arr, 0, len(arr), partitionMedianThree)
    assert arr == sorted(arr)
