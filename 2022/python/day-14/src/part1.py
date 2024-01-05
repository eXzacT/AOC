from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-14.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]

# Changed later in the code
blocked = set()
max_depth = 0


def sand_falling(pos=0+500j) -> bool:
    # Infinite falling, outside of bounds
    if pos.real > max_depth:
        return False

    # Keep falling
    if pos not in blocked:
        return sand_falling(pos+1)
    else:
        # Are both left and right positions also rocks?
        if pos-1j in blocked and pos+1j in blocked:
            blocked.add(pos-1)  # Settle it right above
            return True
        elif pos-1j in blocked:
            return sand_falling(pos+1j)  # Right is blocked, fall left
        else:
            return sand_falling(pos-1j)  # Left is blocked, fall right


def part1(data: list[str]) -> int:
    global max_depth
    for line in data:
        coords = line.split(' -> ')
        # Pairing 0th with 1st, 1st with 2nd, 2nd with 3rd etc., and converting to complex numbers
        for idx in range(len(coords)-1):
            start_y, start_x = map(int, coords[idx].split(','))
            end_y, end_x = map(int, coords[idx+1].split(','))

            step = -1 if end_y < start_y or end_x < start_x else 1
            blocked.update(complex(i, j) for i in range(start_x, end_x+step, step)
                           for j in range(start_y, end_y+step, step))

    max_depth = max(blocked, key=lambda pos: pos.real).real

    count = 0
    while sand_falling():
        count += 1

    return count


if __name__ == "__main__":
    print(part1(data))  # 644
