def is_armstrong_number(number: int) -> bool:
    number_of_digits = len(str(number))
    armstrong = sum([int(digit) ** number_of_digits for digit in str(number)])
    return number == armstrong
