import random

def generate_lotto_card():
  
    lotto_card = {
        'B': [],
        'I': [],
        'N': [],
        'G': [],
        'O': []
    }


    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }


    for letter in lotto_card.keys():
        lotto_card[letter] = random.sample(ranges[letter], 5)

    return lotto_card

def display_lotto_card(lotto_card):
 
    print(" B   I   N   G   O")
    print("--------------------")
    
   
    for i in range(5):
        row = []
        for letter in 'BINGO':
            row.append(f"{lotto_card[letter][i]:<2}") 
        print(" ".join(row))

if __name__ == "__main__":
   
    card = generate_lotto_card()
    display_lotto_card(card)
