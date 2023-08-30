from heap_median import heap_add_and_maintain


def test_median_small_array() -> None:
    arr = [
        28, 7, 32, 13, 21, 3, 4, 26, 12, 36, 18, 9, 23, 1, 25, 16, 11, 5, 34,
        29, 38, 37, 10, 33, 19, 30, 14, 2, 27, 8, 17, 31, 40, 35, 15, 24, 20,
        39, 6, 22
    ]
    medians = 0
    for number in arr:
        medians += heap_add_and_maintain(number)
    assert medians % len(arr) == 15


def test_median_large_array():
    with open('tests/LargeArrayMedian.txt', 'r') as file:
        integers = file.read()
    arr = [int(x) for x in integers.split()]
    medians = 0
    for number in arr:
        medians += heap_add_and_maintain(number)
    assert medians % len(arr) == 1213
