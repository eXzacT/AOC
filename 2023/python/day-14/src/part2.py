import os
from dotenv import load_dotenv

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-14.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]

WIDTH = 100 if __name__ == '__main__' else 10


def rotate_by_90(grid: str):
    return ''.join(grid[-WIDTH + i::-WIDTH] for i in range(WIDTH))


def tilt_forward(grid: str):
    '''
    Simulate gravity upwards by sorting parts in reverse order
    O will be placed before . because 'O' has a bigger ascii value than '.'
    Each column is split by # and sorted, then put back together
    We end up with a list of sorted columns which we then transpose to get rows
    '''
    columns = [grid[i::WIDTH] for i in range(WIDTH)]
    columns = ['#'.join([''.join(sorted(subcol, reverse=True))
                         for subcol in col.split('#')]) for col in columns]
    return ''.join([''.join(row) for row in list(zip(*columns))])


def count_load(grid: str):
    columns = [grid[i::WIDTH] for i in range(WIDTH)]
    # return sum(sum(i for i, c in enumerate(reversed(col), 1)if c == 'O') for col in columns)
    return sum(sum(i for i, c in zip(range(WIDTH, 0, -1), col) if c == 'O') for col in columns)


def part2(input_list: str, cycles: int) -> int:
    grid = ''.join(input_list)
    cycle = 0
    memo = {}
    found_cycle = False
    while cycle < cycles:

        # Tilt once, then rotate and tilt 3 times, then rotate once to get original rotation
        grid = tilt_forward(grid)
        for _ in 'WSE':
            grid = tilt_forward(rotate_by_90(grid))
        grid = rotate_by_90(grid)

        cycle += 1

        # Without this extra flag we would get inside multiple times
        if not found_cycle and (found_cycle := grid in memo):
            # How often does the cycle repeat
            cycle_length = cycle - memo[grid]
            # Skip as far as we can without going over wanted cycles
            cycle += cycle_length * ((cycles - cycle) // cycle_length)
        else:
            memo[grid] = cycle

    return count_load(grid)


if __name__ == "__main__":
    print(part2(file_contents, 1_000_000_000))  # 104533
