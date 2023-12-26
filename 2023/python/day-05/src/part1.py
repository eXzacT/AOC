from dotenv import load_dotenv
import os
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-05.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


'''
    Seed 79, soil 81, fertilizer 81, water 81, light 74, 
        temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, 
        temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, 
        temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, 
        temperature 34, humidity 35, location 35.
'''


def part1(lines: list[str]) -> int:
    # First line contains the start locations(aka seeds)
    lines_iter = iter(lines)
    start_locations = [(int(num), False)  # Keeps track if num was changed
                       for num in re.findall(r'\d+', next(lines_iter))]

    for line in lines_iter:

        if ':' in line:
            # Reset bool flag so the numbers can be changed again later
            start_locations = [(loc_info[0], False)
                               for loc_info in start_locations]

        # Process only lines that have numerical values
        found_nums = [int(num) for num in re.findall(r'\d+', line)]
        if found_nums:
            start = found_nums[1]
            end = start + found_nums[2]
            diff = start - found_nums[0]

            start_locations = [
                (loc_info[0]-diff, True)
                if not loc_info[1] and start <= loc_info[0] < end
                else loc_info
                for loc_info in start_locations
            ]

    return min(start_locations)[0]


if __name__ == "__main__":
    print(part1(file_contents))  # 662197086
