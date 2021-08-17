"""Password checker takes a user input and checks for the correct length.
 If correct it prints the same amount of '*'"""

MIN_LENGTH = 2


def get_password():
    """Retrieve users password."""
    print("\nPlease enter a valid password")
    print(f"Password must be greater than {MIN_LENGTH} characters in length.")
    password = input(">>> ")
    is_valid(password)
    return password


def is_valid(password):
    """Determines if password is valid"""
    if len(password) < MIN_LENGTH:
        print(f"Error, your {len(password)} character password is invalid.")
        get_password()
        return False
    else:
        print(f"Success, your {len(password)} character password is valid.")
        asterisk_printer(password)
        return True


def asterisk_printer(password):
    """Calculate the amount of characters in the password and print the same amount of '*'. """
    for i in range(len(password)):
        print('*', end='')


get_password()

