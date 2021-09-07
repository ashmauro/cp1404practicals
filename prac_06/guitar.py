"""
CP1404/CP5632 Practical - Guitar class.
"""


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        """Return guitar info."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate age"""
        self.age = 2021 - self.year
        return self.age

    def is_vintage(self):
        """Check if vintage"""
        if self.age >= 50:
            return True
        else:
            return False
