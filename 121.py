import random

def generate_lottery_numbers():
    return sorted(random.sample(range(1, 50), 6))

if __name__ == "__main__":
    print("Ваши лотерейные номера:", *generate_lottery_numbers())
