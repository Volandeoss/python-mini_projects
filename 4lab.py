import doctest


def sum_num(number):
    """

    param:
        number (int): цілочисельний тип данних

    Returns:
        int: повертає суму чисел від 0 до number
    >>> sum_num(5)
    15
    >>> sum_num(23)
    276
    >>> sum_num(12)
    78
    >>> sum_num("husifdg")
    0
    """
    try:
        number = int(number)
    except:
        number = 0

    if number < 0:
        number = 0

    return sum(range(0, number + 1))


if __name__ == "__main__":
    doctest.testmod()
    print("Works")
