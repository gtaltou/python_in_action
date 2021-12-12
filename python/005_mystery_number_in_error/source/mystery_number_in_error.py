import random

mystery_number = random.randint(0, 10)
number = input("What is the mystery number?")
number = int(number)

if number > mystery_number:
    print(f"The mystery number is smaller than {number}")
elif number < mystery_number:
    print(f"The mystery number is greater than {number}")
else:
    print("Congratulations, you found the mystery number!")