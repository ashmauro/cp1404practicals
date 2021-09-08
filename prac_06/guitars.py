"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
"""
from prac_06.guitar import Guitar


def main():
    """Get guitar info."""
    guitars = []

    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = int(input("Cost: "))
    #     add_guitar = Guitar(name, year, cost)
    #     guitars.append(add_guitar)
    #     print(add_guitar, "Added.")
    #     name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars != []:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage() == True:
                print(f"Guitar {i + 1}: {guitar.name} ({guitar.year}), worth ${guitar.cost} (vintage)")
            else:
                print(f"Guitar {i +1}: {guitar.name} ({guitar.year}), worth ${guitar.cost}")


main()
