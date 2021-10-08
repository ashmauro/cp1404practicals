"""
CP1404/CP5632 Practical
Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():

    hummer = SilverServiceTaxi("Hummer", 100, 2)
    hummer.drive(18)
    print(hummer)
    print(hummer.get_fare())


main()
