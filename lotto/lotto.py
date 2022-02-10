import random


def lotto():
    numbers = []
    i = 0
    while i < 6:
        numbers.append(random.randint(1, 49))
        i += 1
    numbers.sort()
    return numbers


print(lotto())
