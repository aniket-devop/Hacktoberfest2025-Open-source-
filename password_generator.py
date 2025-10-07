import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all
    all_chars = letters + digits + symbols

    # Ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid pattern
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
