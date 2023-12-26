from dotenv import load_dotenv
from heapq import heappop, heappush
import os


load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-17.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): int(c) for i, row in enumerate(file)
            for j, c in enumerate(row.strip())}

HEIGHT, WIDTH = (141, 141) if __name__ == '__main__' else (13, 13)


def part1(data: dict):
    final_pos = complex(HEIGHT-1, WIDTH-1)
    x = 0  # Just used so the heaps can compare if they have the same heat so far
    seen = set()
    # heat, helper x variable, start pos, direction
    stack = [(0, 0, 0+0j, 1), (0, 0, 0+0j, 1j)]

    while stack:
        heat_lost, _, pos, dir = heappop(stack)
        if pos == final_pos:
            return heat_lost

        if (pos, dir) in seen:
            continue
        seen.add((pos, dir))

        # Go left and right from where we're currently going
        for d in [1j/dir, -1j/dir]:
            for i in range(1, 3+1):  # Possible to do 1 or 3 steps
                if pos+d*i in data:  # Did we go out of bounds?
                    # Calculate heat loss from next i steps and add it to the heap
                    heat = sum(data[pos+d*j] for j in range(1, i+1))
                    heappush(stack, (heat_lost+heat, (x := x+1), pos+d*i, d))


if __name__ == "__main__":
    print(part1(data))  # 1138
