"""A school teacher requires a small program
 that would allow primary school students to
  learn about various number sequences.
  The teacher is interested in a simple menu-driven
  program that has the following choices
  (where x and y are inputs the user enters once at the
   start of the program)"""

MENU = """A - Show even numbers from x to y\nB - Show the odd numbers between from x to y
C - Show the squares from x to y\nQ - Quit the program"""
print(MENU)
choice = input(">>> ").upper()

x_value = int(input("What is your x value? "))
y_value = int(input("What is your y value? "))

while choice != "Q":

    if choice == "A":
        if x_value % 2 == 0:
            for i in range(x_value, y_value, 2):
                print(i, end=' ')
        else:
            for i in range(x_value + 1, y_value, 2):
                print(i, end=' ')
    elif choice == "B":
        if x_value % 2 != 0:
            for i in range(x_value + 1, y_value, 2):
                print(i, end=' ')
        else:
            for i in range(x_value, y_value, 2):
                print(i, end=' ')
    elif choice == "C":
        for i in range(x_value, y_value, 1):
            print(i, end=' ')


