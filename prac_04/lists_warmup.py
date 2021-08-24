"""
CP1404
code for lists-warmup in prac_04
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
# Ans: 3

# numbers[-1]
# Ans: 2

# numbers[3]
# Ans: 1

# numbers[:-1]
# Ans: 3, 1, 4, 1, 5, 9

# numbers[3:4]
# Ans: 1

# 5 in numbers
# Ans: true

# 7 in numbers
# Ans: False

# "3" in numbers
# Ans: False

# numbers + [6, 5, 3]
# Ans: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# 2.Change the last element of numbers to 1
numbers[-1] = 1

# 3.Get all the elements from numbers except the first two (slice)
slice_numbers = numbers[2 :]

# 4.Check if 9 is an element of numbers
9 in numbers
