"""
CP1404/CP5632 - Practical
Broken program to determine score status - extension
"""
from random import randint

MENU = """How many grades? """


def main():
    """Obtain the amount of grades the user wants."""
    print(MENU)
    number_of_grades = int(input(">>> "))
    scores = []

    for i in range(number_of_grades):
        n = randint(0, 100)
        scores.append(n)
    print(scores)
    result_grade = score_grade(scores)
    print(result_grade)


def score_grade(scores):
    """Determine what grade the user got."""
    for score in scores:
        if score < 0 or score > 100:
            return "Invalid Score"
        elif score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()
