from dotenv import load_dotenv
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-23.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): c for i, row in enumerate(file.readlines())
            for j, c in enumerate(row.strip()) if c != '#'}

WIDTH, HEIGHT = (141, 141) if __name__ == '__main__' else (23, 23)


def part1(data: dict[complex, str]) -> int:
    stack = [(0+1j, 1, set())]
    arrow_dir = {'>': 1j, '<': -1j, '^': -1, 'v': 1, '.': 0}
    end = (HEIGHT-1)*1+(WIDTH-2)*1j
    max_path = 0

    while stack:
        pos, dir, seen = stack.pop()
        # Not on a valid position, going against the arrow or been here before
        if pos not in data or arrow_dir[data[pos]] == -dir or pos in seen:
            continue

        seen = seen.copy()  # So seen isn't shared across different paths
        seen.add(pos)

        if pos == end:
            max_path = max(max_path, len(seen))
        for d in [1, -1, -1j, 1j]:
            stack.append((pos+d, d, seen))

    return max_path-1  # -1 for start position


if __name__ == "__main__":
    print(part1(data))  # 2362
