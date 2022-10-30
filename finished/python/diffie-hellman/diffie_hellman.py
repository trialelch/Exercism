import random

def private_key(p: int):
    if p < 1:
        raise ValueError("Key must be greater than 1")
    key = random.randint(1, p - 1)
    print(f"Key: {key}, p = {p - 1}")
    return key


def public_key(p, g, private):
    print(f"p: {p}, g: {g}, Key_Num: {private}")
    # First solutions was calculation with  the private_key function
    # This one is right
    return (g ** private) % p


def secret(p, public, private):
    return public ** private % p
