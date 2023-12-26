from dotenv import load_dotenv
from functools import reduce
from operator import add
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-18.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def shoelace_formula(verts: list[complex]) -> int:
    return reduce(add, [verts[i].imag*verts[i+1].real-verts[i].real*verts[i+1].imag for i in range(len(verts)-1)], 0)


def part2(data: list[str]) -> int:
    start_pos = 0+0j
    total_steps = 0
    verts = [start_pos]

    for line in data:

        _, _, color = line.split(' ')
        dir = {'0': 1j, '1': 1, '2': -1j, '3': -1}[color[-2]]
        steps = int(color[2:-2], 16)

        total_steps += steps
        start_pos += steps*dir
        verts.append(start_pos)

    return shoelace_formula(verts)/2+total_steps/2+1


def part2_v2(data: list[str]) -> int:
    prev_pos = 0+0j
    res = 0

    for line in data:

        _, _, color = line.split(' ')
        dir = {'0': 1j, '1': 1, '2': -1j, '3': -1}[color[-2]]
        steps = int(color[2:-2], 16)

        # Move to the new direction, use the shoelace formula for prev and curr pos
        curr_pos = prev_pos+steps*dir
        res += (prev_pos.imag*curr_pos.real -
                prev_pos.real*curr_pos.imag)/2+steps/2
        prev_pos = curr_pos

    return res+1


if __name__ == "__main__":
    print(part2(data))  # 96556251590677
    print(part2_v2(data))
