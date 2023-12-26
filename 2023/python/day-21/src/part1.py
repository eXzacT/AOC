from dotenv import load_dotenv
from collections import deque
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-21.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): c if c != '.' else 0 for i, row in enumerate(file.readlines())
            for j, c in enumerate(row)}

WIDTH, HEIGHT = (131, 131) if __name__ == "__main__" else (11, 11)


def print_data(data: dict[complex, str], final_positions: set[complex]) -> None:
    print()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pos = complex(i, j)
            if pos in final_positions:
                print('O', end='')
            else:
                print(data[pos], end='')
        print()


def part1(data: dict[complex, str], goal_steps: int):
    (start,) = (pos for pos, c in data.items() if c == 'S')

    seen = set()
    queue = deque([(start, 0, 0)])
    while queue:
        pos, val, steps = queue.popleft()
        if steps == goal_steps:
            continue
        for d in [1, -1, -1j, 1j]:
            new_pos = pos+d
            # Out of bounds or hit a wall
            if not 0 <= new_pos.imag < WIDTH or not 0 <= new_pos.real < HEIGHT or data[new_pos] == '#':
                continue
            if new_pos not in seen:
                seen.add(new_pos)
                data[new_pos] = val+1
                queue.append((new_pos, val+1, steps+1))

    # print_data(data, set())
    # Only even numbers not including 0
    return sum(isinstance(val, int) and val % 2 == 0 and val != 0 for val in data.values())


if __name__ == "__main__":
    print(part1(data, 64))  # 3762
