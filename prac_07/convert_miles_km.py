"""
CP1404 Practical 07
Miles to Kilmeters converter Kivy GUI program
Ashley Mauro
Started 21/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class ConvertMilesApp(App):
    """ConvertMilesApp is a kivy app that converts miles to km's."""
    output = StringProperty()

    def build(self):
        """Build Kivy app from kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self):
        """handle_conversion executes the conversion form miles to km's."""
        value = self.validate_input()
        self.root.ids.output_label.text = str(float(value) * CONVERSION_FACTOR)

    def validate_input(self):
        """Validates if the input was a number"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, increment):
        """Increments input up by 1."""
        value = self.validate_input() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_conversion()


ConvertMilesApp().run()