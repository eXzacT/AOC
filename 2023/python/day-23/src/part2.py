from dotenv import load_dotenv
from collections import defaultdict
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-23.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): c for i, row in enumerate(file.readlines())
            for j, c in enumerate(row.strip()) if c != '#'}

WIDTH, HEIGHT = (141, 141) if __name__ == '__main__' else (23, 23)


def find_junctions(data: dict[complex, list[complex]]) -> list[complex]:
    return [pos for pos, adjacent in data.items()if len(adjacent) > 2
            or len(adjacent) == 1]  # Or start/end


def find_neighbours(junctions: list[complex], data: dict[complex, str]) -> dict[tuple[complex, int]]:
    # For each junction branch out and see where they lead, also store distance
    roads = defaultdict(list)
    for j in junctions:
        # Go in every direction starting from each junction, with a step counter
        stack = [(j,  [1, -1, -1j, 1j], 0)]
        while stack:
            pos, dirs, dist = stack.pop()

            # Not on a valid position
            if pos not in data:
                continue

            # Found a connecting junction, store its position and distance to it
            if pos in junctions and pos != j:  # Ignore self
                roads[j].append((pos, dist))
                continue

            for d in dirs:
                # Can only keep going in that same direction, or 90°L/R
                stack.append((pos+d, [d, -1j/d, 1j/d], dist+1))

    return roads


def traverse(roads: dict[complex, list[tuple[complex, int]]]):

    max_dist = 0
    stack = [(0, set(), 1j)]

    while stack:
        dist, seen, current_node = stack.pop()
        seen = seen.copy()  # So every stack has it's own copy

        if current_node not in seen:
            seen.add(current_node)
            max_dist = max(max_dist, dist)

            # Go in each direction and add the updated distance
            for next_node, edge_dist in roads[current_node]:
                if next_node not in seen:
                    stack.append((dist + edge_dist, seen, next_node))

    return max_dist


def part2(data: dict[complex, str]):
    # Mapping every position to a list of valid adjacent positions
    adjacent = {pos: [pos+d for d in (1, -1, 1j, -1j) if pos+d in data]
                for pos in data}

    return traverse(find_neighbours(find_junctions(adjacent), data))


if __name__ == "__main__":
    print(part2(data))  # 6538
