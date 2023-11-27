# Create a Python script that does the following:
# Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.

import os
import sys


def read_and_print_files(directory_path: str, file_extension: str) -> None:
    try:
        if not os.path.isdir(directory_path):
            raise ValueError("Invalid directory path")

        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"Contents of {filename}:\n{content}\n{'=' * 50}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect usage")
    else:
        dir_path = sys.argv[1]
        f_extension = sys.argv[2]
        read_and_print_files(dir_path, f_extension)
