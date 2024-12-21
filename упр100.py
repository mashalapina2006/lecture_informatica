import random
def generate_password():
    length = random.randint(7, 10) 
    password = ''.join(chr(random.randint(33, 126)) for __ in range(length))
    return password
if __name__ == "__main__":
    random_password = generate_password()
    print(f"Сгенерированный пароль: {random_password}")
