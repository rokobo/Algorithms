from two_sum_algorithm import solve_2_sum


def test_small_array():
    assert solve_2_sum([-2, 0, 0, 4], 0, 4) == 2


def test_large_array():
    with open('./tests/LargeArray2Sum.txt', 'r') as file:
        integers = file.read()
    arr = {int(x) for x in integers.split()}
    assert solve_2_sum(arr, -10000, 10000) == 427
