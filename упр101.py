import random
import string
def generate_license_plate():
    if random.choice([True, False]):
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        digits = ''.join(random.choices(string.digits, k=3))
        license_plate = f"{letters}{digits}"
    else:
        digits = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        license_plate = f"{digits}{letters}"
        return license_plate
if __name__ == "__main__":
    random_license_plate = generate_license_plate()
    print(f"Сгенерированный номерной знак: {random_license_plate}")
