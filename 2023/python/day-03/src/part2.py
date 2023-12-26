from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-03.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part2(input_data: str) -> int:
    sum_nums = 0

    # Iterate through each line in the input_data, excluding the first and last lines
    for curr_row in range(1, len(input_data) - 1):
        current_row_stripped = input_data[curr_row].strip()

        for col, char in enumerate(current_row_stripped):
            if char == '*':
                found_numbers = []

                # Check the 3x3 square around the symbol for numbers
                for row_idx in range(curr_row - 1, curr_row + 2):
                    temp_row_stripped = input_data[row_idx].strip()

                    for num_match in re.finditer(r'\d+', temp_row_stripped):
                        num_start, num_end = num_match.span()

                        # Check if the number overlaps the symbol
                        if num_start - 1 <= col <= num_end:
                            found_numbers.append(int(num_match.group()))

                if char == '*':
                    # Calculate the gear ratio only if there are 2 hits
                    if len(found_numbers) == 2:
                        sum_nums += found_numbers[0] * found_numbers[1]

    return sum_nums


if __name__ == '__main__':

    print(part2(file_contents))
