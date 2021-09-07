"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
"""
#
from prac_06.guitar import Guitar


def main():
    """ """
    # Gibson L-5 CES (1922) : $16,035.40

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1000000)
    print(f"{guitar.name} get_age() - Expected 99. Got {guitar.get_age()} ")
    print(f"{other.name} get_age() - Expected 8. Got {other.get_age()} ")
    print(f"{guitar.get_age()}-year old guitar is_vintage(), Expected True. Got {guitar.is_vintage()}")
    print(f"{other.get_age()}-year old guitar is_vintage(), Expected False. Got {other.is_vintage()}")



main()
