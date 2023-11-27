# Create a Python script that calculates the total size of all files in a directory provided as a command line
# argument. The script should:
#
# Use the sys module to read the directory path from the command line. Utilize the os module to iterate through all
# the files in the given directory and its subdirectories. Sum up the sizes of all files and display the total size
# in bytes. Implement exception handling for cases like the directory not existing, permission errors, or other file
# access issues.


import os
import sys


def calculate_total_size(directory_path: str) -> None:
    total_size = 0

    try:
        if not os.path.isdir(directory_path):
            raise ValueError("Invalid directory path")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in {directory_path}: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage")
    else:
        dir_path = sys.argv[1]

        calculate_total_size(dir_path)
