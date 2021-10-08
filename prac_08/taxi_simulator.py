"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Code for taxi simulator."""
    current_taxi = None
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_bill = 0.00
    choice = input(">>> ").upper()

    while choice != 'Q':

        if choice == 'D':
            if current_taxi != None:
                taxis[current_taxi].start_fare()
                distance = get_distance()
                taxis[current_taxi].drive(distance)
                cost_of_trip = taxis[current_taxi].get_fare()
                current_bill += cost_of_trip
                print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, cost_of_trip))
                print("Bill to date: ${:.2f}".format(current_bill))
            else:
                print("You need to choose a taxi before you can drive")
        elif choice == 'C':
            current_taxi = get_taxi(taxis)
            print("Bill to date: ${:.2f}".format(current_bill))
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Total trip cost: ${:.2f}".format(current_bill))
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


def get_taxi(taxis):
    """ Returns chosen taxi."""
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))

    taxi_chosen = None
    valid_input = False
    while not valid_input:
        try:
            taxi_chosen = int(input("Choose taxi: "))

            if taxi_chosen >= len(taxis):
                print("Invalid choice")

            elif taxi_chosen < 0:
                print("Error, input must be great than or equal to 0")

            else:
                valid_input = True

        except ValueError:
            print("Enter a valid number")
    return taxi_chosen


def get_distance():
    """ Returns distance wanted to drive."""
    distance = 0
    try:
        distance = int(input("Drive how far? "))
    except ValueError:
        print("Please enter a number.")
    return distance


main()
