import random

def toss_coin():
    return 'О' if random.randint(0, 1) == 0 else 'Р'

def simulate_tosses():
    count = 0
    results = []
    last_tosses = []

    while True:
        toss = toss_coin()
        results.append(toss)
        last_tosses.append(toss)
        count += 1
        if len(last_tosses) >= 3 and last_tosses[-1] == last_tosses[-2] == last_tosses[-3]:
            break

    print(''.join(results), end=' ')
    return count

def main():
    total_attempts = 0
    simulations = 10

    for _ in range(simulations):
        attempts = simulate_tosses()
        print(f"| Попытки: {attempts}")
        total_attempts += attempts

    average_attempts = total_attempts / simulations
    print(f"\nСреднее количество попыток: {average_attempts:.2f}")

if __name__ == "__main__":
    main()







