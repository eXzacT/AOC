from dotenv import load_dotenv
import os
import re
from functools import reduce

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-06.txt'
file_contents = list(open(filename, 'r'))


def part1(input_list: list[str]) -> int:
    race_times = [int(num) for num in re.findall(r'\d+', input_list[0])]
    distances_to_beat = [int(num) for num in re.findall(r'\d+', input_list[1])]

    total_ways_to_win = 1
    way_to_win = 0

    for idx in range(len(race_times)):
        for held_time in range(1, race_times[idx]):
            remaining_time = race_times[idx]-held_time
            total_crossed = held_time*remaining_time
            if total_crossed > distances_to_beat[idx]:
                way_to_win += 1

        total_ways_to_win *= way_to_win
        way_to_win = 0

    return total_ways_to_win


if __name__ == "__main__":
    print(part1(file_contents))
