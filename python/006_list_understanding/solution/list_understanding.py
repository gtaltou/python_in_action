numbers = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
number_even = [i for i in numbers if i % 2 == 0]
print(number_even)

# ---------------------------------------------------- #

numbers = range(-10, 10)
number_positive= [i for i in numbers if i >= 0]
print(number_positive)

# ---------------------------------------------------- #

numbers = range(5)
number_dual = [i * 2 for i in numbers]
print(number_dual)

# ---------------------------------------------------- #

numbers = range(10)
numbers_reverse = [i if i % 2 == 0 else -i for i in numbers]
print(numbers_reverse)