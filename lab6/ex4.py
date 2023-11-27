# Write a Python script that counts the number of files with each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv). Use the os module to list all files in the
# directory. Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts. Include
# error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.

import os
import sys


def count_files_by_extension(directory_path: str) -> None:
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        if not os.path.isdir(directory_path):
            raise ValueError(f"Invalid directory path: {directory_path}")
        if not os.access(directory_path, os.R_OK):
            raise PermissionError(f"No read permissions for directory: {directory_path}")
        extension_counts = {}
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                _, file_extension = os.path.splitext(filename)
                extension = file_extension.lower()

                if extension in extension_counts:
                    extension_counts[extension] += 1
                else:
                    extension_counts[extension] = 1

        if not extension_counts:
            print("No files found in the directory.")
        else:
            print("File counts by extension:")
            for extension, count in extension_counts.items():
                print(f"{extension}: {count} files")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage")
    else:
        dir_path = sys.argv[1]
        count_files_by_extension(dir_path)
