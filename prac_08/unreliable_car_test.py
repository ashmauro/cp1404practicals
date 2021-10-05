""""
CP1404/CP5632 Practical
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Code to test UnreliableCar class."""

    good_car = UnreliableCar("More reliable", 100, 92)
    bad_car = UnreliableCar("Less reliable", 100, 8)
    good_car.drive(40)
    bad_car.drive(40)
    print(good_car)
    print(bad_car)


main()
