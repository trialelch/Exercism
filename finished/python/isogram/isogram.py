"""Exercism / Exercise Isogram"""


def is_isogram(string: str) -> bool:
    """Checks if the string is an isogram"""

    only_alphabet = [char.lower() for char in string if char.isalpha()]
    return len(only_alphabet) == len(set(only_alphabet))
