from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-09.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]


def direction(dist: complex) -> complex:
    '''credit 4HbQ on reddit, I didn't know we could subtract booleans'''
    return complex((dist.real > 0) - (dist.real < 0), (dist.imag > 0) - (dist.imag < 0))


def part2(data: list[str]) -> int:
    tail_seen = set([0+0j])
    dir_map = {'U': -1, 'D': 1, 'R': 1j, 'L': -1j}
    rope = [0+0j]*10  # All the knots are on position 0

    for line in data:
        d, n = line.split(' ')
        d, n = dir_map[d], int(n)
        for _ in range(n):
            # Move the head and propagate movement to the children
            rope[0] += d
            for i in range(1, 10):
                dist = rope[i-1] - rope[i]
                if abs(dist) < 2:  # Current knot is somewhere around the previous
                    break
                else:  # Move the current knot in the direction of the previous knot
                    rope[i] += direction(dist)
                    if i == 9:  # Tail
                        tail_seen.add(rope[i])

    return len(tail_seen)


if __name__ == "__main__":
    print(part2(data))  # 2653
