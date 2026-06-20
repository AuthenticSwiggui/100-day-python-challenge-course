import random

# 1. Letters 'a' through 'z' generated from a string split
letters = list("abcdefghijklmnopqrstuvwxyz")

# 2. Numbers 0 through 9 using range()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Exactly 9 common special characters
special_characters = list("!@#$%^&*()")



print("Stupid password generator")
num_letters = int(input("How many letters?\n"))
num_numbers = int(input("How many numbers?\n"))
num_characters = int(input("How many characters?\n"))

password = ""

for i in range (0, num_letters, 1):
    password += random.choice(letters)

for i in range (0, num_characters, 1):
    password += random.choice(special_characters)

for i in range (0, num_numbers, 1):
    password += str(random.choice(numbers))
print(f"Easy Password: {password}")

password = []


for i in range (0, num_letters + 1, 1):
    password.append(random.choice(letters))

for i in range (0, num_characters + 1, 1):
    password.append(random.choice(special_characters))

for i in range (0, num_numbers, 1):
    password.append(str(random.choice(numbers)))

random.shuffle(password)
print(password)

password_string = ""
for character in password:
    password_string += character

print(password_string)