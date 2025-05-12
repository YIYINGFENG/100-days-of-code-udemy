import random

# Define character pools
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

# Welcome message
print("🔐 Welcome to the PyPassword Generator!")

# Get user input
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Generate password characters
password = []

for _ in range(num_letters):
    password.append(random.choice(letters))

for _ in range(num_symbols):
    password.append(random.choice(symbols))

for _ in range(num_numbers):
    password.append(random.choice(numbers))

# Shuffle the characters
random.shuffle(password)

# Combine into a single string
final_password = ''.join(password)

# Output the result
print(f"\n✅ Your generated password is: {final_password}")
