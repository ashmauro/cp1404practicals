"""
CP1404/CP5632 - Practical
Broken program to determine score status - extension
"""
import random

MENU = """How many grades? """


def main():
    """Obtain the amount of grades the user wants."""
    print(MENU)
    number_of_grades = input(">>> ")

    for i in number_of_grades:
        score = random.randint(0, 100)
    result_grade = score_grade(score)
    print(result_grade)
    print(score)


def score_grade(score):
    """Determine what grade the user got."""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
