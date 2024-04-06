import random
import string

def generate_password(length=12):
    """
    Generate a random password of the specified length.
    Default length is 12 characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password (default is 12): "))

    password = generate_password(length)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
