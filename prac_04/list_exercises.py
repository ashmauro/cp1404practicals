"""
CP1404/CP5632 Practical
Code for list_exercises.py
"""

# 1. Number list
print("""Please enter 5 numbers""")

number_list =[]
for number in range(5):
    number = int(input("Number: ")) # Obtains numbers from user.
    number_list.append(number)

# Prints various facts about the list of numbers.
print("The first number is: {}".format(number_list[0]))
print("The last number is: {}".format(number_list[-1]))
print("The smallest number is: {}".format(min(number_list)))
print("the largest number is: {}".format(max(number_list)))
print("The average of all numbers is: {}".format((sum(number_list) / len(number_list))))

#2. Security checker
username_list = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("What is your username? ")  # Obtains username

if user_name in username_list:
    print("Access granted, username exists")
else:
    print("Access denied, username does not exist")
