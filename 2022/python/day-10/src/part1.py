from dotenv import load_dotenv
from itertools import accumulate
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-10.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]
    file.seek(0)
    # addx 15 gets replaced with 0,15, counts as 2 cycles
    data_v2 = [*map(lambda c: int(c) if c[-1].isdigit() else 0,
                    file.read().split())]


def part1(data: list[str]) -> int:
    signal_strength = cycle = 0
    register_value = 1
    for line in data:
        action, *rest = line.split(' ')

        if action == 'addx':
            value = int(rest[0])

            for _ in range(2):
                cycle += 1
                if cycle % 40 == 20:
                    signal_strength += cycle * register_value

            register_value += value

        elif action == 'noop':
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * register_value

    return signal_strength


def part1_v2(data: list[int]) -> int:
    '''credit goes to 4HbQ on reddit, beautiful solution as always'''
    signal_strength = 0
    for cycle, value in enumerate(accumulate([1]+data), start=1):
        signal_strength += cycle * value if cycle % 40 == 20 else 0
    return signal_strength


if __name__ == "__main__":
    print(part1(data))  # 14560
    print(part1_v2(data_v2))
