"""
CP1404/CP5632 Practical
Sort files into folders
"""

import os
import shutil


def main():
    """Main function"""
    os.chdir('FilesToSort')
    extensions = get_file_extensions()
    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
    sort_files()


def get_file_extensions():
    """Get file extensions"""
    file_extensions = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            if file_extension not in file_extensions:
                file_extensions.append(file_extension)
    return file_extensions


def sort_files():
    """Move files into specific folders"""
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            shutil.move(filename, file_extension)


main()
