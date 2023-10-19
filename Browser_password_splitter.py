import os
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

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

def display_header():
    print(Fore.CYAN + r'''

  _____                          _____                                    _    _____       _ _ _   _            
 |  __ \                        |  __ \                                  | |  / ____|     | (_) | | |           
 | |  | | __ _ _ __ ___   __ _  | |__) |_ _ ___ _____      _____  _ __ __| | | (___  _ __ | |_| |_| |_ ___ _ __ 
 | |  | |/ _` | '_ ` _ \ / _` | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  \___ \| '_ \| | | __| __/ _ \ '__|
 | |__| | (_| | | | | | | (_| | | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |  ____) | |_) | | | |_| ||  __/ |   
 |_____/ \__,_|_| |_| |_|\__,_| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_____/| .__/|_|_|\__|\__\___|_|   
                                                                                    | |                         
                                                                                    |_|                         

    ''' + Style.RESET_ALL)
    print(Fore.YELLOW + "Split your CSV file into smaller parts for easy management." + Style.RESET_ALL)

def main():
    display_header()

    # Input
    input_file = input(Fore.YELLOW + "Enter the name of the CSV file containing passwords in the current Folder: " + Style.RESET_ALL)
    max_size = int(input(Fore.YELLOW + "Enter the maximum size (in bytes) for each split file: " + Style.RESET_ALL))

    if not os.path.isfile(input_file):
        print(Fore.RED + "File not found. Please make sure the file exists in the current directory." + Style.RESET_ALL)
        return

    output_files = split_file(input_file, max_size)
    
    print("\nFiles have been split into the following parts:")
    for output_file in output_files:
        print(Fore.GREEN + f"- {output_file} ({get_file_size(output_file)} bytes)" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
