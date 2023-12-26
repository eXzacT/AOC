from dotenv import load_dotenv
import os
import re
import math

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-08.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part2(input_list: list[str]) -> int:
    locations_dict = {}
    start_locations = []
    instructions, _, *lines = input_list
    for line in lines:
        location_info: list[str] = re.findall(r'[A-Z]+', line)
        if location_info[0].endswith('A'):
            start_locations.append(location_info[0])
        locations_dict[location_info[0]] = location_info[1], location_info[2]

    steps = 0
    cycles = []
    while start_locations:
        side = instructions[steps % len(instructions)]
        start_locations = [locations_dict[loc]
                           [0 if side == 'L' else 1] for loc in start_locations]
        steps += 1

        # Add how many steps it was necessary to reach Z and remove that loc
        for loc in start_locations:
            if loc.endswith('Z'):
                cycles.append(steps)
                start_locations.remove(loc)

    # The result is equal to LCM of the steps necessary for each start loc
    return math.lcm(*cycles)


if __name__ == "__main__":
    print(part2(file_contents))  # 22103062509257
