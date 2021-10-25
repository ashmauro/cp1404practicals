"""
CP1404/CP5632 Practical
Sort files into categorised folders
"""

import os
import shutil


def main():
    os.chdir('FilesToSort')
    extension_dict = get_file_extensions()
    sort_files(extension_dict)


def get_file_extensions():
    """Return a dictionary with categories as keys and a list of corresponding extensions as values"""
    file_extensions = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            if file_extension not in file_extensions:
                category = input("What category would you like to sort {} files into? ".format(file_extension))
                file_extensions[file_extension] = category
    return file_extensions


def sort_files(extension_dict):
    """Move files into specific folders"""
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            category = extension_dict[file_extension]
            try:
                os.mkdir(category)
            except FileExistsError:
                print("{} directory already exists".format(category))
            shutil.move(filename, category)


main()
