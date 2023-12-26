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


def print_data(data: dict[complex, str]):
    print('\n')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(data[complex(i, j)], end=' ')
        print()


def part1(data: dict[complex, str]):
    seen = set()
    # Start from 1 position left from top left, for edge case when 1st char is a mirror
    stack = [(0-1j, 0+1j)]
    while stack:
        pos, dir = stack.pop()
        # Only continue if we weren't here OR if we weren't here from this dir
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

    # print_data(data)

    # for pos, _ in seen:
    #     data[pos] = '#'

    # print_data(data)

    return len(set(pos for pos, _ in seen))-1


if __name__ == "__main__":
    print(part1(data))  # 7951
