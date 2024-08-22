import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

while True:
    # Prompt the user for the desired length of the password
    length = input("Enter the desired length of your password (or enter 'q' to quit): ")

    if length.lower() == 'q':
        break

    try:
        # Convert the input to an integer
        length = int(length)

        # Generate a password and print it to the console
        password = generate_password(length)
        print("Your random password is:", password)

    except ValueError:
        # If the input cannot be converted to an integer, print an error message
        print("Invalid input. Please enter a number.")
