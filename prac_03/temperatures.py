"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Obtains user choice of temperature mode and numerical value of temperature"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit}")
        elif choice == 'F':
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
