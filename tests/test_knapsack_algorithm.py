from knapsack_algorithm import max_value_for_weight


def test_small() -> None:
    knapsack = [(3, 4), (2, 3), (4, 2), (4, 3)]
    assert max_value_for_weight(knapsack, 6) == 8


def test_medium() -> None:
    with open("tests/LargeArrayKnapsack1.txt") as file:
        knapsack = [tuple(map(int, i.split())) for i in file]
    assert max_value_for_weight(knapsack, 10_000) == 2493893


def test_large() -> None:
    with open("tests/LargeArrayKnapsack2.txt") as file:
        knapsack = [tuple(map(int, i.split())) for i in file]
    assert max_value_for_weight(knapsack, 2_000_000) == 4243395
