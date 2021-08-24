"""
CP1404/CP5632 Practical
quick_picks code
"""
import random

TOTAL_NUMBERS = 6
MIN_RANDOM = 1
MAX_RANDOM = 45


def main():
    """Displays lists"""
    quick_picks = amount_picks()
    generate_picks(quick_picks)


def amount_picks():
    """Obtains the amount of quick picks"""
    number_picks = int(input("How many quick picks would you like? "))
    while number_picks <= 0:
        print("Error, cannot have negative number of quick picks")
        number_picks = int(input("How many quick picks would you like? "))
    return number_picks


def generate_picks(number_picks):
    """ Generates list of random numbers based on number of picks"""
    for i in range(number_picks):
        quick_pick_list = []  # Generates number of lists
        for number in range(TOTAL_NUMBERS):
            random_number = random.randint(MIN_RANDOM, MAX_RANDOM)  # Generates 6 random numbers between limits
            while random_number in quick_pick_list:  # Checks to see if number is already in list
                random_number = random.randint(MIN_RANDOM, MAX_RANDOM)  # Generates new number if double-up
            quick_pick_list.append(random_number)  # appends rand number to list
            quick_pick_list.sort()  # Sorts list into ascending numbers

        print_quick_pick = ""
        for random_number in quick_pick_list:
            print_quick_pick += f"{random_number:2}"
        print(print_quick_pick)


main()
