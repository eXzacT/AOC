from dotenv import load_dotenv
from itertools import accumulate
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-10.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]
    file.seek(0)
    data_v2 = [*map(lambda c: int(c) if c[-1].isdigit() else 0,
                    file.read().split())]


def part2(data):
    cycle = 0
    sprite_position = 1
    drawn_image = ""

    for line in data:
        action, *rest = line.split(' ')
        if action == 'addx':
            value = int(rest[0])
            for _ in range(2):
                cycle += 1
                if (cycle-1) % 40-sprite_position in [-1, 0, 1]:
                    drawn_image += '#'
                else:
                    drawn_image += ' '

            sprite_position += value  # Update sprite position immediately after action

        elif action == 'noop':
            cycle += 1
            if (cycle-1) % 40-sprite_position in [-1, 0, 1]:
                drawn_image += '#'
            else:
                drawn_image += ' '

    # Add newline characters between every 40 characters
    drawn_image = '\n'.join([drawn_image[i:i+40]
                            for i in range(0, len(drawn_image), 40)])
    return drawn_image


def part2_v2(data: list[int]) -> str:
    '''credit goes to 4HbQ on reddit, beautiful solution as always'''
    drawn_image = ''
    for cycle, value in enumerate(accumulate([1]+data), start=1):
        drawn_image += '#' if (cycle-1) % 40-value in [-1, 0, 1] else ' '

    # Add newline characters between every 40 characters
    drawn_image = '\n'.join([drawn_image[i:i+40]
                            for i in range(0, len(drawn_image), 40)])
    return drawn_image


if __name__ == "__main__":
    print(part2(data))
    print()
    print(part2_v2(data_v2))
