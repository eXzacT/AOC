import math
from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-03.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part1(input_data: list[str]) -> int:
    sum_nums = 0
    symbols_pos = [(r, c) for r in range(len(input_data)) for c in range(len(input_data))
                   if input_data[r][c] not in '0123456789.']

    for row_idx, row_str in enumerate(input_data):

        for num_match in re.finditer(r'\d+', row_str):
            num_start_idx, num_end_idx = num_match.span()

            for sym_row, sym_col in symbols_pos:

                # Check if the symbol is adjacent to the number
                if sym_row in range(row_idx - 1, row_idx + 2):  # prev,curr,nxt

                    for col in range(num_start_idx, num_end_idx):
                        if sym_col in range(col - 1, col + 2):
                            sum_nums += int(num_match.group())
                            break  # Break to avoid double counting

    return sum_nums


def part1_v2(input_data: list[str]) -> int:
    sum_nums = 0

    # Iterate through lines, skipping the first and last
    for curr_row in range(1, len(input_data)-1):
        prev_row = curr_row - 1
        next_row = curr_row + 1

        current_row_stripped = input_data[curr_row].strip()
        for col, char in enumerate(current_row_stripped):
            # Found a symbol
            if char not in '0123456789.':

                # Check the 3x3 square around the symbol for numbers
                for row_idx in [prev_row, curr_row, next_row]:
                    temp_curr_row_stripped = input_data[row_idx].strip()

                    for num_match in re.finditer(r'\d+', temp_curr_row_stripped):
                        num_start, num_end = num_match.span()
                        # Check if the number overlaps the symbol
                        if num_start-1 <= col <= num_end:
                            sum_nums += int(num_match.group())

    return sum_nums


def part1_and_part2(input_data: list[str]) -> int:
    chars = {(r, c): [] for r in range(len(input_data)) for c in range(len(input_data))
             if input_data[r][c] not in '01234566789.'}

    for r, row in enumerate(input_data):
        for n in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                    for c in range(n.start()-1, n.end()+1)}
            for o in edge & chars.keys():
                chars[o].append(int(n.group()))
    return sum(sum(p) for p in chars.values()), sum(math.prod(p) for p in chars.values() if len(p) == 2)


if __name__ == '__main__':

    print(part1(file_contents))
    print(part1_v2(file_contents))
    print(part1_and_part2(file_contents))
