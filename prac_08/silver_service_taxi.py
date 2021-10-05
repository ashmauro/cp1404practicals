"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from prac_08.taxi import Taxi
from random import randint


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a fanciness factor."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi ."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the current fare."""
        return self.flagfall + super().get_fare()
