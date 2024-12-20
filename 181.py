def can_make_change(target, coins, num_coins):
    if target == 0 and num_coins == 0:
        return True
    if target < 0 or num_coins < 0:
        return False
    for coin in coins:
        if can_make_change(target - coin, coins, num_coins - 1):
            return True
    return False
def main():
    coins = [1, 5, 10, 25]
    amount = float(input("Введите искомую сумму в долларах (например, 1.25): "))
    num_coins = int(input("Введите количество монет: "))
    target = int(amount * 100)
if can_make_change(target, coins, num_coins):
        print(f"Можно собрать сумму {amount} из {num_coins} монет.")
    else:
        print(f"Нельзя собрать сумму {amount} из {num_coins} монет.")
if __name__ == "__main__":
    main()
