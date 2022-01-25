numbers = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
number_even = []
for i in numbers:
    if i % 2 == 0:
       number_even.append(i)

print(number_even)

# ---------------------------------------------------- #

numbers = range(-10, 10)
number_positive = []
for i in numbers:
    if i >= 0:
        number_positive.append(i)

print(number_positive)

# ---------------------------------------------------- #

numbers = range(5)
number_dual = []
for i in numbers:
    number_dual.append(i * 2)

print(number_dual)

# ---------------------------------------------------- #

numbers = range(10)
number_reverse = []
for i in numbers:
    if i % 2 == 0:
       number_reverse.append(i)
    else:
        number_reverse.append(-i)

print(number_reverse)