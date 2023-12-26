from dotenv import load_dotenv
from itertools import combinations
from functools import reduce
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-11.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part2(input_list: list[str]) -> int:
    galaxy_locations = []
    # Mark every column for expansion, later remove found galaxies in those cols
    to_expand_cols = set(i for i in range(len(input_list[0])))
    to_expand_rows = set()

    for row, line in enumerate(input_list):
        cols = [i for i in range(len(line)) if line.startswith('#', i)]
        if not cols:  # Row has no galaxies, mark for doubling
            to_expand_rows.add(row)
            continue

        for col in cols:
            # Found a galaxy in the row, don't double that column loc
            to_expand_cols.discard(col)
            galaxy_locations.append((row, col))

    # Shift the locations by count*1_000_000 times of expanded places before them
    galaxy_locations = [(row + 999_999*sum(row > x for x in to_expand_rows),
                         col + 999_999*sum(col > y for y in to_expand_cols))
                        for (row, col) in galaxy_locations]

    # Accumulate the total of the differences by adding all the combination diff
    total_difference = reduce(lambda carry, c: carry +
                              (abs(c[1][1]-c[0][1]) + abs(c[1][0]-c[0][0])),
                              combinations(galaxy_locations, 2), 0)
    return total_difference


if __name__ == "__main__":
    print(part2(file_contents))  # 622120986954
