'''Exercism / Exercise Resistor Color'''

COLOR_CODE = {'black': 0,
              'brown': 1,
              'red': 2,
              'orange': 3,
              'yellow': 4,
              'green': 5,
              'blue': 6,
              'violet': 7,
              'grey': 8,
              'white': 9}


def color_code(color: str) -> int:
    """The single resistor number by color"""
    return COLOR_CODE[color]


def colors() -> list[str]:
    """Shows all available Resistorcolors ordered by value"""
    return list(COLOR_CODE.keys())
