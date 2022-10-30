
def is_triangle(sides):
    for side in sides:
        if side <=0:
            return False
    return True

def is_valid_triangle(sides):
    if sum(sorted(sides)[:2]) < sorted(sides)[2]:
        return False
    return True


def equilateral(sides):
    if is_triangle(sides):
        return len(set(sides)) == 1
    return False


def isosceles(sides):
    if is_triangle(sides) & is_valid_triangle(sides):
        return len(set(sides)) <= 2
    return False


def scalene(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) == 3
    return False