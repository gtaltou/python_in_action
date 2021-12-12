import random

mystery_number = random.randint(0, 10)
number = input("What is the mystery number ? ")
if not number.isdigit():
    print("Please enter a valid number.")
    exit()

number = int(number)
if number > mystery_number:
    print(f"The mystery number is smaller than {number}")
elif number < mystery_number:
    print(f"The mystery number is greater than {number}")
else:
    print("Congratulations, you found the mystery number!")

