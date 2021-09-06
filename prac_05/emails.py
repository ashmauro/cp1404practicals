"""
CP1404/CP5632 Practical
emails
"""


def main():
    """Create dictionary of emails to names."""
    email_dict = {}
    email = input("Email: ")
    while email != "":
        user_name = get_name(email)
        user_confirmation = input("Is you name {}? (Y or N)".format(user_name))
        if user_confirmation.upper() == "N":
            user_name = input("Name: ")
        email_dict[email] = user_name
        email = input("Email: ")

    for email, name in email_dict.items():
        print("{} {}".format(name, email))


def get_name(email):
    """Extract and return name from email address."""
    user_name = email.split("@")[0]
    parts = user_name.split(".")
    user_name = " ".join(parts).title()
    return user_name


main()
