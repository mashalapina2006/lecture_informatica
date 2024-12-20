import random

def create_deck():
    suits = 'shdc'
    ranks = '23456789TJQKA'
    return [r + s for s in suits for r in ranks]

def shuffle_deck(deck):
    for i in range(len(deck)):
        j = random.randrange(i, len(deck))
        deck[i], deck[j] = deck[j], deck[i]

def deal(num_players, cards_per_player, deck):
    hands = [[] for _ in range(num_players)]
    for i in range(cards_per_player):
        for j in range(num_players):
            hands[j].append(deck.pop(0) if deck else None)
    return [hand for hand in hands if any(hand)]

if __name__ == "__main__":
    deck = create_deck()
    shuffle_deck(deck)
    
    num_players = 4
    cards_per_player = 5
    hands = deal(num_players, cards_per_player, deck)
    
    print("Карты игроков:")
    for i, hand in enumerate(hands):
        print(f"Игрок {i+1}: {hand}")
    
    print("\nОставшиеся карты в колоде:")
    print(deck)
