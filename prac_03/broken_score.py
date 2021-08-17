"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Obtain users score, or generate random score."""
    score = float(input("Enter score: "))
    result_grade = score_grade(score)
    print(result_grade)

    score = random.randint(0, 100)
    result_grade = score_grade(score)
    print(result_grade)


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
