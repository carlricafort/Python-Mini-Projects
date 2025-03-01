import random

# Define character sets
letters = list("abcdefghijklmnopqrstuvwxyz")  # Shorter way to define letters
numbers = list("0123456789")
spec_chars = list("!@#$%&")

# Welcome message
print("Welcome to Kev's Password Generator")

# User input
insert_letter = int(input("How many letters would you like in your password? \n"))
insert_number = int(input("How many numbers would you like in your password? \n"))
insert_char = int(input("How many special characters would you like in your password? \n"))

# Generate 5 random passwords and store them in a list
passwords = []

for i in range(1,6):
    password = []
    
    # Add random letters
    for char in range(insert_letter):
        password.append(random.choice(letters))

    # Add random numbers
    for char in range(insert_number):
        password.append(random.choice(numbers))

    # Add special characters
    for char in range(insert_char):
        password.append(random.choice(spec_chars))

    # Shuffle the password to mix characters
    random.shuffle(password)

    # Convert list to string and add to passwords list
    passwords.append("".join(password))

print(f"These are you passwords {passwords}")