"""
CP1404/CP5632 Practical - programming language class.
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Initialise a language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return if language is dynamic or not"""
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False

    def __str__(self):
        """Return language info."""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"