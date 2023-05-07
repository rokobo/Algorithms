from src.CountingInversions import CountInversions
from random import randint


def test_inversions() -> None:
    assert CountInversions([1, 2, 3, 4, 5], 5)[1] == 0
    assert CountInversions([5, 4, 3, 2, 1], 5)[1] == 10
    assert CountInversions([1, 3, 5, 2, 4, 6], 6)[1] == 3
    assert CountInversions([7, 6, 5, 4, 3, 2, 1], 7)[1] == 21
    assert CountInversions([2, 4, 1, 3, 5], 5)[1] == 3
    assert CountInversions([10, 20, 30, 40, 50], 5)[1] == 0
    assert CountInversions([1, 1, 1, 1, 1], 5)[1] == 0
    assert CountInversions([2, 1], 2)[1] == 1
    assert CountInversions([1], 1)[1] == 0
    assert CountInversions([], 0)[1] == 0
    assert CountInversions([1, 2, 3, 5, 4], 5)[1] == 1
    assert CountInversions([1, 5, 3, 2, 4], 5)[1] == 4
    assert CountInversions([5, 4, 3, 2, 1, 6], 6)[1] == 10
    assert CountInversions([6, 5, 4, 3, 2, 1], 6)[1] == 15
    assert CountInversions([1, 3, 2], 3)[1] == 1
    assert CountInversions([1, 5, 3, 2, 4, 6], 6)[1] == 4
    assert CountInversions([10, 15, 20, 25, 30, 35, 40], 7)[1] == 0
    assert CountInversions([40, 30, 20, 10], 4)[1] == 6
    assert CountInversions([1, 2, 3, 4, 5, 6, 7], 7)[1] == 0
    assert CountInversions([7, 6, 5, 4, 3, 2, 1, 8], 8)[1] == 21
    assert CountInversions([1, 4, 2, 5, 3], 5)[1] == 3
    assert CountInversions([1, 2, 4, 3, 5], 5)[1] == 1
    assert CountInversions([10, 20, 15, 25, 30, 5, 35], 7)[1] == 6
    assert CountInversions([2, 1, 4, 3, 6, 5], 6)[1] == 3
    assert CountInversions([1, 6, 3, 4, 5, 2], 6)[1] == 7


def test_random_max_inversions_4() -> None:
    # A n sized array can have at most n(n-1)/2 inversions
    for _ in range(100000):
        random_list = [randint(1, 10) for _ in range(4)]
        assert CountInversions(random_list, 4)[1] < 7


def test_random_max_inversions_5() -> None:
    # A n sized array can have at most n(n-1)/2 inversions
    for _ in range(100000):
        random_list = [randint(1, 10) for _ in range(5)]
        assert CountInversions(random_list, 5)[1] < 11


def test_random_max_inversions_6() -> None:
    # A n sized array can have at most n(n-1)/2 inversions
    for _ in range(100000):
        random_list = [randint(1, 10) for _ in range(6)]
        assert CountInversions(random_list, 6)[1] < 16


def test_100K_integer_array() -> None:
    with open('tests/LargeArrayInversions.txt', 'r') as file:
        integers = file.read()
    integers_list = [x for x in integers.split()]
    assert CountInversions(integers_list, len(integers_list))[1] == 2397819672
