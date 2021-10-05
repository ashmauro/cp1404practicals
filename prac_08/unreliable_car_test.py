""""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Code to test UnreliableCar class."""

    car = UnreliableCar("Unreliable 1", 100, 50)
    car.drive(40)
    print(car)


main()
