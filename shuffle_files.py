import random

import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Shuffle the lines of a file.")
parser.add_argument('--files', metavar='file', type=str, nargs='+', help="File(s) to shuffle", required=True)
args = parser.parse_args()

for title in args.files:
    try:
        # Read the file into a list
        with open(f'{title}', 'r') as file:
            lines = file.readlines()
            print(f'{title} has {len(lines)} lines.')

        # Shuffle the lines
        random.shuffle(lines)

        # Write the shuffled lines back to a file
        with open(f'{title}', 'w') as file:
            file.writelines(lines)
            print(f'Shuffled {len(lines)} lines in {title}.txt.')

        print("The lines have been randomly ordered.")

    except FileNotFoundError:
        print(f"Error: {title}.txt not found.")