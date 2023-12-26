from dotenv import load_dotenv
import os
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-08.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part1(input_list: list[str]) -> int:

    locations_dict = {}
    instructions, _, *lines = input_list
    for line in lines:
        location_info = re.findall(r'[A-Z]+', line)
        locations_dict[location_info[0]] = location_info[1], location_info[2]

    loc = 'AAA'
    steps = 0
    while loc != 'ZZZ':
        side = instructions[steps % len(instructions)]
        loc = locations_dict[loc][0 if side == 'L' else 1]
        steps += 1

    return steps


if __name__ == "__main__":
    print(part1(file_contents))
