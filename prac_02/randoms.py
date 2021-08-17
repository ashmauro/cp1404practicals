import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
"""The smallest number will be 5 and the largest will be 20. 
The upper and lower limits are inclusive in the selection"""

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
"""The smallest number you can see is 3 and the largest is 9, no it could have produced a 4
The only numbers in this print will be ODD"""

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
"""Generating a random number between 2.5 and 5.5. The uniform returns a random floating point. The smallest """


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))


