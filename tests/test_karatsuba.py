from src.KaratsubaAlgorithm import split, karatsuba


def test_split() -> None:
    assert split("14", 1) == (1, 4)
    assert split("1536", 2) == (15, 36)
    assert split("167", 1) == (1, 67)
    assert split("67247", 2) == (67, 247)
    assert split("873836", 3) == (873, 836)


def test_single_digit() -> None:
    assert karatsuba(2, 5) == 10
    assert karatsuba(2, 8) == 16
    assert karatsuba(4, 1) == 4
    assert karatsuba(5, 3) == 15
    assert karatsuba(9, 5) == 45
    assert karatsuba(6, 9) == 54
    assert karatsuba(7, 5) == 35
    assert karatsuba(3, 4) == 12
    assert karatsuba(2, 9) == 18
    assert karatsuba(4, 2) == 8
    assert karatsuba(1, 5) == 5
    assert karatsuba(4, 7) == 28
    assert karatsuba(4, 4) == 16
    assert karatsuba(6, 7) == 42
    assert karatsuba(6, 4) == 24
    assert karatsuba(5, 9) == 45
    assert karatsuba(6, 7) == 42
    assert karatsuba(9, 7) == 63
    assert karatsuba(8, 7) == 56
    assert karatsuba(6, 9) == 54


def test_multiple_digits() -> None:
    assert karatsuba(9462, 3993) == 37781766
    assert karatsuba(2144, 7444) == 15959936
    assert karatsuba(7023, 2729) == 19165767
    assert karatsuba(1239, 1734) == 2148426
    assert karatsuba(681, 3862) == 2630022
    assert karatsuba(5234, 8236) == 43107224
    assert karatsuba(5993, 425) == 2547025
    assert karatsuba(3545, 6272) == 22234240
    assert karatsuba(1502, 6068) == 9114136
    assert karatsuba(208, 7666) == 1594528
    assert karatsuba(8393, 1208) == 10138744
    assert karatsuba(9180, 2778) == 25502040
    assert karatsuba(9836, 3736) == 36747296
    assert karatsuba(9194, 5391) == 49564854
    assert karatsuba(2035, 9175) == 18671125
    assert karatsuba(8907, 1076) == 9583932
    assert karatsuba(503, 7916) == 3981748
    assert karatsuba(742, 1709) == 1268078
    assert karatsuba(9975, 5244) == 52308900
    assert karatsuba(298, 1358) == 404684
    assert karatsuba(7937, 5689) == 45153593
    assert karatsuba(7392, 2894) == 21392448
    assert karatsuba(1632, 7303) == 11918496
    assert karatsuba(2070, 686) == 1420020
    assert karatsuba(7236, 402) == 2908872
    assert karatsuba(4343, 4957) == 21528251
    assert karatsuba(2859, 6926) == 19801434
    assert karatsuba(6578, 4852) == 31916456
    assert karatsuba(4814, 5047) == 24296258
    assert karatsuba(687, 4807) == 3302409
    assert karatsuba(4357, 4748) == 20687036
    assert karatsuba(393, 7495) == 2945535
    assert karatsuba(2217, 1541) == 3416397
    assert karatsuba(8482, 4380) == 37151160
    assert karatsuba(1994, 6938) == 13834372
    assert karatsuba(4421, 4345) == 19209245
    assert karatsuba(7137, 1253) == 8942661
    assert karatsuba(3324, 1517) == 5042508
    assert karatsuba(8239, 3760) == 30978640
    assert karatsuba(8222, 1167) == 9595074
    assert karatsuba(4679, 4697) == 21977263
    assert karatsuba(1637, 2781) == 4552497
    assert karatsuba(3969, 2493) == 9894717
    assert karatsuba(9406, 767) == 7214402
    assert karatsuba(1501, 2008) == 3014008
    assert karatsuba(8152, 6764) == 55140128
    assert karatsuba(8541, 775) == 6619275
    assert karatsuba(3227, 5060) == 16328620
    assert karatsuba(4381, 3932) == 17226092
    assert karatsuba(6258, 8205) == 51346890
