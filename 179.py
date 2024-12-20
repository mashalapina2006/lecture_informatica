def recursive_sqrt(n, guess=1.0):
    new_guess = (guess + n / guess) / 2
    if abs(new_guess**2 - n) < 1e-12:
        return new_guess
    else:
        return recursive_sqrt(n, new_guess)
def main():
    numbers = [4, 9, 16, 25, 2, 50]
    for number in numbers:
        result = recursive_sqrt(number)
        print(f"Квадратный корень из {number} ≈ {result}")
if __name__ == "__main__":
    main()
