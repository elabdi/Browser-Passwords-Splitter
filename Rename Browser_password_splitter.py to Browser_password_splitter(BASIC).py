# Password Splitter Script
# Author: ILIAS ELABDI
# Version: 1.0

import os

def split_file(input_file, max_size):
    """
    Splits a CSV file into smaller parts, each under a specified maximum size.

    Args:
        input_file (str): Name of the input CSV file.
        max_size (int): Maximum size (in bytes) for each split file.

    Returns:
        List of str: Names of the generated split files.
    """
    with open(input_file, "r") as infile:
        header = next(infile)
        output_files = []
        output_data = []
        current_size = 0
        part_number = 1

        for line in infile:
            if current_size + len(line) > max_size:
                output_filename = f"part{part_number}.csv"
                with open(output_filename, "w") as outfile:
                    outfile.write(header)
                    outfile.writelines(output_data)
                output_files.append(output_filename)
                output_data = []
                current_size = 0
                part_number += 1

            output_data.append(line)
            current_size += len(line)

        # Write the last part if there's any data left
        if output_data:
            output_filename = f"part{part_number}.csv"
            with open(output_filename, "w") as outfile:
                outfile.write(header)
                outfile.writelines(output_data)
            output_files.append(output_filename)

        return output_files

def get_file_size(filename):
    """Returns the size of a file in bytes."""
    return os.path.getsize(filename)

def main():
    print("=== Password Splitter ===")
    
    # Input
    input_file = input("Enter the name of the CSV file containing passwords in current Folder: ")
    max_size = int(input("Enter the maximum size (in bytes) for each split file: "))

    if not os.path.isfile(input_file):
        print("File not found. Please make sure the file exists in the current directory.")
        return

    output_files = split_file(input_file, max_size)
    
    print("\nFiles have been split into the following parts:")
    for output_file in output_files:
        print(f"- {output_file} ({get_file_size(output_file)} bytes)")

if __name__ == "__main__":
    main()
