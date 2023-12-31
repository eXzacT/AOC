from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-09.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]


def part1(data: list[str]) -> int:
    tail_seen = set([0+0j])
    dir_map = {'U': -1, 'D': 1, 'R': 1j, 'L': -1j}
    head_pos = tail_pos = 0+0j
    for line in data:
        d, n = line.split(' ')
        d, n = dir_map[d], int(n)
        for _ in range(n):
            prev_head_pos = head_pos
            head_pos += d
            # If we moved too far from tail then move it where the head was
            if abs(head_pos-tail_pos) >= 2:
                tail_pos = prev_head_pos
                tail_seen.add(tail_pos)

    return len(tail_seen)


if __name__ == "__main__":
    print(part1(data))  # 6563
