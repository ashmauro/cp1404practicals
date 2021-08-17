"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("\tInvalid password!")
        password = input("> ")

def is_valid_password(password):
    """Determine if the provided password is valid."""
    if MIN_LENGTH > len(password)  or MAX_LENGTH < len(password):
        print("\tYour {}-character password is invalid length: {}".format(len(password), password))
        print(f"\tYour password must be in between {MIN_LENGTH} and {MAX_LENGTH} characters long.")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if SPECIAL_CHARS_REQUIRED:
        if count_special < 1:
            print(f"\tError, your password must have special characters")
            return False

    if count_lower < 1:
        print(f"\tError, your password must have 1 or more lowercase characters.")
        return False
    elif count_upper < 1:
        print(f"\tError, your password must have 1 or more UPPERCASE characters.")
        return False
    elif count_digit < 1:
        print(f"\tError, your password must have 1 or more NUMBERS.")
        return False
    else:
        print("\tSuccess! Your password is valid!")
        print(f"\tYour password has {count_lower} lowercase letters.")
        print(f"\tYour password has {count_upper} uppercase letters.")
        print(f"\tYour password has {count_digit} numbers.")
        print(f"\tYour password has {count_special} special characters.")

    return True

main()
