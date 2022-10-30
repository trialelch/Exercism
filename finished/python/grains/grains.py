def square(number):
    if (number <= 0) | (number > 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number -1)


def total():
    all = [2 ** (num-1) for num in range(1,64+1)]
    return sum(all)
