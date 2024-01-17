from dotenv import load_dotenv
from itertools import cycle
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-17.txt'
with open(filename, 'r') as file:
    data = file.read().strip()

CHAMBER_LEFT_WALL = 0
CHAMBER_RIGHT_WALL = 8
BLOCKS = 2022


def print_chamber(placed: set[complex], max_y) -> None:
    print()
    for y in range(max_y, 0, -1):
        for x in range(1, 8):
            if complex(x, y) in placed:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(data: str) -> int:
    # Y position will change later by doing max_y+IMAG part
    blocks = [(3+4j, 4+4j, 5+4j, 6+4j),  # - shape
              (3+5j, 4+5j, 5+5j, 4+4j, 4+6j),  # + shape
              (3+4j, 4+4j, 5+4j, 5+5j, 5+6j),  # Reversed L shape
              (3+4j, 3+5j, 3+6j, 3+7j),  # | shape
              (3+4j, 4+4j, 3+5j, 4+5j)]  # square shape

    # Set ground as placed, usually I use x(REAL part) for row and y(IMAG part) for column,
    # but in this problem it made more sense to use cartesian coordinate system
    max_y = 0
    placed = set([1+0j, 2+0j, 3+0j, 4+0j, 5+0j, 6+0j, 7+0j])

    data = cycle(data)
    # Spawn the first block
    i = 0
    block_parts_positions = blocks[i]

    while i < BLOCKS:
        # Get the next direction
        direction = next(data)
        # if i == 4:
        #     print_chamber(placed,max_y)
        #     return

        match direction:
            case '<':
                new_pos = [pos-1 for pos in block_parts_positions]
                # Is any position blocked by either another block or a wall?
                if not any(pos in placed or pos.real == CHAMBER_LEFT_WALL for pos in new_pos):
                    block_parts_positions = new_pos
            case '>':
                new_pos = [pos+1 for pos in block_parts_positions]
                # Is any position blocked by either another block or a wall?
                if not any(pos in placed or pos.real == CHAMBER_RIGHT_WALL for pos in new_pos):
                    block_parts_positions = new_pos

        # Can we move the block down?
        new_pos = [pos-1j for pos in block_parts_positions]
        if not any(pos in placed for pos in new_pos):
            block_parts_positions = new_pos
        else:
            # Place this block down, update highest position
            placed.update({pos for pos in block_parts_positions})
            max_rock_height = max(pos.imag for pos in block_parts_positions)
            max_y = max(max_y, max_rock_height)

            # Then spawn a new block
            i += 1
            block_parts_positions = blocks[i % len(blocks)]
            block_parts_positions = [complex(pos.real, pos.imag+max_y)
                                     for pos in block_parts_positions]

    return max_y


if __name__ == "__main__":
    print(part1(data))  # 3163
