def square_of_sum(number: int) -> int:
    return sum(range(number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    return sum(elem ** 2 for elem in range(number + 1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
