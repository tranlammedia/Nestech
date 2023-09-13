import random

# Define a function to generate a random password
def generate_password(length):
    # Define the character set for the password
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?"
    # Use random.choices() to generate a password of the given length
    password = "".join(random.choices(char_set, k=length))
    return password

# Ask the user for the length of the password
while True:
    try:
        length = int(input("Enter the length of the password (must be a number): "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Generate the password and print it
password = generate_password(length)
print("Your password is:", password)
