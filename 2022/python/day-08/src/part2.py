from dotenv import load_dotenv
from functools import reduce
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-08.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): int(c) for i, row in enumerate(file)
            for j, c in enumerate(row.strip())}


WIDTH, HEIGHT = (99, 99) if __name__ == "__main__" else (5, 5)


def part2(data: dict[complex, str]) -> int:
    best_scenic_score = 0
    for i in range(1, WIDTH-1):
        for j in range(1, HEIGHT-1):
            pos = complex(i, j)
            tree_height = data[pos]
            direction_scores = []
            for d in [1, -1, -1j, 1j]:
                new_pos = pos+d
                curr_dirr_score = 1
                # Keep going in the current direction until blocked by a taller tree
                while data[new_pos] < tree_height:
                    new_pos += d
                    if new_pos not in data:  # Out of bounds
                        break
                    curr_dirr_score += 1

                direction_scores.append(curr_dirr_score)

            if (s := reduce(lambda x, y: x*y, direction_scores)) > best_scenic_score:
                best_scenic_score = s

    return best_scenic_score


if __name__ == "__main__":
    print(part2(data))  # 479400
