from dotenv import load_dotenv
from collections import defaultdict
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-22.txt'
with open(filename, 'r') as file:
    data = re.findall(r'\d+', file.read())
    data = [int(num) for num in data]

    # Group every six numbers together, and sort based on last number
    data = [data[i:i+6] for i in range(0, len(data), 6)]
    data.sort(key=lambda x: x[-1])


# Minimum points where bricks can fall onto
bottom_positions: dict[tuple[int, int], int] = dict()


def pos_after_falling(brick_id: int, start: tuple[int, int, int], end: tuple[int, int, int]) -> dict[int, list[tuple[int, int, int]]]:
    positions = generate_3d_space(start, end)
    max_depth = 1  # So the first brick goes to 1
    for pos in positions:
        if (pos[0], pos[1]) not in bottom_positions:
            continue
        depth = bottom_positions[(pos[0], pos[1])]
        # Pick the highest overlap because we can't force the brick to go lower
        max_depth = max(max_depth, depth+1)

    # How far down can we put this brick?
    lowest = min(pos[2] for pos in positions)
    diff = max_depth-lowest

    # Update bottom positions and update all z values for the current brick
    new_positions: tuple[int, int, int] = []
    for x, y, z in positions:
        new_positions.append((x, y, z+diff))
        bottom_positions.update({(x, y): z+diff})

    return {brick_id: new_positions}


def generate_3d_space(start: tuple[int, int, int], end: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    result = []
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for z in range(start[2], end[2] + 1):
                result.append((x, y, z))
    return result


def total_carnage(bricks: dict[int, list[tuple[int, int, int]]]):
    above = defaultdict(set)
    below = defaultdict(set)

    # Convert brick positions into a set for faster lookup
    positions = {brick: set(positions) for brick, positions in bricks.items()}

    # Build the support relationships
    for curr_brick, curr_positions in positions.items():
        for other_brick, other_positions in positions.items():
            # Don't compare the brick with itself
            if curr_brick != other_brick:
                for pos in curr_positions:
                    above_pos = (pos[0], pos[1], pos[2] + 1)
                    if above_pos in other_positions:
                        above[curr_brick].add(other_brick)
                        below[other_brick].add(curr_brick)

    # A brick can be removed if all bricks above it have alternative support
    removable_bricks = []
    for brick in bricks:
        if all(any(support != brick for support in below[above_brick]) for above_brick in above[brick]):
            removable_bricks.append(brick)

    # Bricks that are not safe to remove are the opposite of removable
    to_break = [brick for brick in bricks.keys()
                if brick not in removable_bricks]

    total_fallout = 0
    for brick in to_break:
        affected = set([brick])
        queue = [brick]

        while queue:
            current_brick = queue.pop()
            # For every brick above the current, if it no longer has support, it falls
            for above_brick in above[current_brick]:
                # Check if all the bricks below have been affected
                if all(below in affected for below in below[above_brick]):
                    affected.add(above_brick)
                    queue.append(above_brick)

        total_fallout += len(affected)

    # Don't count the bricks we broke manually
    return total_fallout-len(to_break)


def part2(data: list[int]) -> int:
    bricks: dict[int, list[tuple[int, int, int]]] = {}

    for i, line in enumerate(data, start=1):
        start = tuple(line[:3])
        end = tuple(line[3:])
        bricks.update(pos_after_falling(i, start, end))

    return total_carnage(bricks)


if __name__ == "__main__":
    print(part2(data))  # 72352
