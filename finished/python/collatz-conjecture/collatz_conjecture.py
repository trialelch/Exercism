def steps(number: int) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_counter = 0
    while number != 1:
        # changed the new comparison after looking at the community solutions
        # easier to read
        # checking for even / odd
        if number % 2 == 0:
            # Hint from community solution, Make sure it is always a int
            number //= 2
        else:
            number = number * 3 + 1
        step_counter += 1

    return step_counter
