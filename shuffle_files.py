import random

inputs = ['shakespeare', "slang", "combined_data"]

for title in inputs:
    # Read the file into a list
    with open(f'{title}.txt', 'r') as file:
        lines = file.readlines()
        print(len(lines))

    # Shuffle the lines
    random.shuffle(lines)

    # Write the shuffled lines back to a file
    with open(f'{title}.txt', 'w') as file:
        file.writelines(lines)
        print(len(lines))

    print("The lines have been randomly ordered.")