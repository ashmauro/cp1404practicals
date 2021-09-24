"""
CP1404 Practical 07
Dynamic Labels Kivy GUI program
Ashley Mauro
Started 21/09/2021
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


LABEL_LIST = ["Jim", "Jeffery", "Ashley", "Ben"]


class DynamicLabels(App):
    """ DynamicLabels is a Kivy App for creating dynamic labels """
    status = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in LABEL_LIST:
            temp_button = Button(text=name)
            self.root.ids.entries_main.add_widget(temp_button)
            temp_button.bind(on_release=self.press_entry)
        return self.root

    def press_entry(self, on_release):
        print(on_release.text)


DynamicLabels().run()