from quickselect import QuickSelect


def test_length_3() -> None:
    assert QuickSelect([1, 2, 3], 0) == 1
    assert QuickSelect([1, 2, 3], 1) == 2
    assert QuickSelect([1, 2, 3], 2) == 3


def test_length_6() -> None:
    assert QuickSelect([6, 5, 4, 3, 2, 1], 0) == 1
    assert QuickSelect([6, 5, 4, 3, 2, 1], 1) == 2
    assert QuickSelect([6, 5, 4, 3, 2, 1], 2) == 3
    assert QuickSelect([6, 5, 4, 3, 2, 1], 3) == 4
    assert QuickSelect([6, 5, 4, 3, 2, 1], 4) == 5
    assert QuickSelect([6, 5, 4, 3, 2, 1], 5) == 6


def test_length_7() -> None:
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 0) == 1
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 1) == 2
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 2) == 3
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 3) == 4
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 4) == 5
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 5) == 6
    assert QuickSelect([7, 3, 1, 5, 2, 6, 4], 6) == 7


def test_length_9() -> None:
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 0) == 1
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 1) == 2
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 2) == 3
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 3) == 4
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 4) == 5
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 5) == 6
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 6) == 7
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 7) == 8
    assert QuickSelect([9, 3, 7, 1, 2, 8, 6, 5, 4], 8) == 9


def test_length_10() -> None:
    assert QuickSelect([8, 2, 5, 9, 1, 6, 3, 10, 4, 7], 0) == 1
    assert QuickSelect([8, 2, 5, 9, 1, 6, 3, 10, 4, 7], 3) == 4
    assert QuickSelect([8, 2, 5, 9, 1, 6, 3, 10, 4, 7], 5) == 6
    assert QuickSelect([8, 2, 5, 9, 1, 6, 3, 10, 4, 7], 8) == 9
    assert QuickSelect([8, 2, 5, 9, 1, 6, 3, 10, 4, 7], 9) == 10
    assert QuickSelect([56, 40, 61, 7, 4, 61, 71, 48, 58, 16], 9) == 71
