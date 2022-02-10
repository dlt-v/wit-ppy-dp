import random


def karty(input):
    colors = input.split(',')
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for color in colors:
        for card in cards:
            deck.append(f'{color}({card})')
    random.shuffle(deck)
    return deck


print(karty('wiosna,lato,jesien,zima'))
