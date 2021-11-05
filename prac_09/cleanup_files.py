"""
CP1404/CP5632 Practical
cleanup_files
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    temp = []
    for index, character in enumerate(new_name):  # Iterate through each character in filename

        if character.isupper() and index != 0:  # if character is uppercase and index of character is not 0

            if new_name[index-1] != '_':  # if the character before is not an underscore than add one
                temp.append('_')
                temp.append(character)
            else:
                temp.append(character)
        # if character before is a bracket and character is lowercase than change to upper case.
        elif new_name[index - 1] == "(" and character.islower():
            temp.append(character.upper())
        else:
            temp.append(character)
    # updated_name = "".join(temp)
    # print(updated_name)
    return "".join(temp)


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


# main()
demo_walk()
