# Write a script using the os module that renames all files in a specified directory to have a sequential number
# prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or
# files that can't be renamed.

import os
import sys


def rename_files_with_sequence(directory_path: str) -> None:
    try:
        if not os.path.isdir(directory_path):
            raise ValueError("Invalid directory path")
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        for i, filename in enumerate(files, start=1):
            original_path = os.path.join(directory_path, filename)
            new_filename = f"file{i}.{filename.split('.')[-1]}"  # maintain file extension
            new_path = os.path.join(directory_path, new_filename)
            os.rename(original_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage")
    else:
        dir_path = sys.argv[1]
        rename_files_with_sequence(dir_path)
