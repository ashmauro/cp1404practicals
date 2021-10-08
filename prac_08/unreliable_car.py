"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car based on reliability comparison."""
        reliability_comparison = randint(0,100)
        if reliability_comparison <= self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
