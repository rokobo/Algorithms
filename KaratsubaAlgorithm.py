threshold = 10


def karatsuba(x: int, y: int) -> int:
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))

    # threshold for switching to standard multiplication
    if n < threshold:
        return x * y

    # split x and y into two parts of m size
    m = n // 2
    a, b = split(x_str, m)
    c, d = split(y_str, m)

    # compute the three intermediary values
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # combine intermediate products using formula
    return ac * 10**(2*m) + ad_bc * 10**m + bd


def split(number_str: str, digits: int) -> tuple[int, int]:
    left_half = int(number_str[:digits])
    right_half = int(number_str[digits:])
    return left_half, right_half
