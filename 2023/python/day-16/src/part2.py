from dotenv import load_dotenv
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-16.txt'
with open(filename, 'r') as file:
    # Complex numbers represent the position and values are characters on that pos
    data = {complex(i, j): c for i, row in enumerate(file)
            for j, c in enumerate(row.strip())}

WIDTH = 110 if __name__ == '__main__' else 10
HEIGHT = 110 if __name__ == '__main__' else 10


def part2(data: dict[complex, str]):
    max_energized = 0
    # These are entry points just outside the boundaries from each side
    entry_points = [[(-1+i*1j, 1)] for i in range(WIDTH)]
    entry_points.extend([[(WIDTH+i*1j, -1)] for i in range(WIDTH)])
    entry_points.extend([[(i-1j, 1j)] for i in range(HEIGHT)])
    entry_points.extend([[(i+HEIGHT*1j, -1j)] for i in range(HEIGHT)])

    for entry_point in entry_points:
        seen = set()
        stack = entry_point
        while stack:
            pos, dir = stack.pop()
            while not (pos, dir) in seen:
                seen.add((pos, dir))
                pos += dir
                match data.get(pos):
                    case '|':  # Moves down and remembers to move up later
                        dir = 1
                        stack.append((pos, -dir))
                    case '-':
                        dir = 1j  # Moves right and remembers to move left later
                        stack.append((pos, -dir))
                    case '/':  # Pairs W-N and E-S, coming from west->now north, and opposite
                        dir = -1j/dir
                        # -complex(dir.imag, dir.real)
                    case '\\':  # Pairs W-S and E-N, coming from west->now south, and opposite
                        dir = 1j/dir
                        # complex(dir.imag, dir.real)
                    case None:
                        break

        max_energized = max(max_energized, len(set(pos for pos, _ in seen))-1)

    return max_energized


def part2_v2(stack: list[tuple[complex, complex]], data: dict[complex, str]):
    seen = set()
    while stack:
        pos, dir = stack.pop()
        while not (pos, dir) in seen:
            seen.add((pos, dir))
            pos += dir
            match data.get(pos):
                case '|':  # Moves down and remembers to move up later
                    dir = 1
                    stack.append((pos, -dir))
                case '-':
                    dir = 1j  # Moves right and remembers to move left later
                    stack.append((pos, -dir))
                case '/':  # Pairs W-N and E-S, coming from west->now north, and opposite
                    dir = -1j/dir
                    # dir = -complex(dir.imag, dir.real)
                case '\\':  # Pairs W-S and E-N, coming from west->now south, and opposite
                    dir = 1j/dir
                    # dir = complex(dir.imag, dir.real)
                case None:
                    break

    return len(set(pos for pos, _ in seen))-1


if __name__ == "__main__":
    print(part2(data))  # 8148
    # Generate all the positions just outside the boundaries, forming a square
    print(max(map(lambda pos_and_dir: part2_v2(pos_and_dir, data), ([
          (pos-dir, dir)] for dir in (1, -1, 1j, -1j) for pos in data if pos-dir not in data))))
