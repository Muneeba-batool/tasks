import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    if length < 1:23
        print("Invalid length. Please enter a positive integer.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the password generator
password_generator()
