import random
import string

def generate_password(length):
    if length < 6:
        return "Password too short! Use at least 6 characters."

    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print("=== Secure Password Generator ===")

try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number!")