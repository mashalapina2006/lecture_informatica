import random

def create_deck():
    suits = 'shdc'
    ranks = '23456789TJQKA'
    return [r + s for s in suits for r in ranks]

def shuffle_deck(deck):
    for i in range(len(deck)):
        j = random.randrange(i, len(deck))
        deck[i], deck[j] = deck[j], deck[i]

if __name__ == "__main__":
    deck = create_deck()
    print("Исходная колода:\n", deck)
    shuffle_deck(deck)
    print("\nПеретасованная колода:\n", deck)
