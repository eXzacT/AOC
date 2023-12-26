from dotenv import load_dotenv
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-18.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def flood_fill(edges: set[complex]) -> int:
    """
    Count the number of positions inside the boundary defined by 'edges'
    This is done by using flood fill from outside then subtracting from total area
    """
    # Boundary tracking: Find min and max coordinates
    min_x = min(edges, key=lambda z: z.real).real
    max_x = max(edges, key=lambda z: z.real).real
    min_y = min(edges, key=lambda z: z.imag).imag
    max_y = max(edges, key=lambda z: z.imag).imag

    # Initialize variables for flood fill
    seen = set()
    queue = [complex(x, min_y) for x in range(int(min_x), int(max_x)+1)]
    queue += [complex(x, max_y) for x in range(int(min_x), int(max_x)+1)]
    queue += [complex(min_x, y) for y in range(int(min_y), int(max_y)+1)]
    queue += [complex(max_x, y) for y in range(int(min_y), int(max_y)+1)]
    outside_count = 0

    # Flood fill to count outside positions
    while queue:
        pos = queue.pop()
        # Skip if we've been here, it's a boundary or out of bounds
        if pos in edges or pos in seen or not min_x <= pos.real <= max_x or not min_y <= pos.imag <= max_y:
            continue

        seen.add(pos)
        outside_count += 1
        for dir in [1, -1, 1j, -1j]:
            queue.append(pos+dir)

    total_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return total_area - outside_count


def point_in_polygon(edges: set[complex]) -> int:
    """
    Count the number of positions inside the boundary defined by 'edges'
    Then add that number to number of edges
    """
    # Boundary tracking: Find min and max coordinates
    min_x = int(min(edges, key=lambda z: z.real).real)
    max_x = int(max(edges, key=lambda z: z.real).real)
    min_y = int(min(edges, key=lambda z: z.imag).imag)
    max_y = int(max(edges, key=lambda z: z.imag).imag)

    inside = 0
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            pos = complex(i, j)
            if pos in edges:  # Only compare non edges
                continue

            # How many times we hit an edge by projecting in a diagonal
            hits = 0
            while min_x <= pos.real <= max_x and min_y <= pos.imag <= max_y:
                pos = pos+1+1j
                if pos in edges:
                    # Ignore corner connecting south and west
                    if pos-1j in edges and pos+1 in edges:
                        continue
                    # Ignore corner connecting north and east
                    if pos+1j in edges and pos-1 in edges:
                        continue

                    hits += 1

            if hits % 2 == 1:  # Odd means we were inside
                inside += 1

    return inside+len(edges)


def part1(data: list[str]) -> int:
    edges = set()
    start_pos = 0+0j

    for line in data:

        dir, steps, _ = line.split(' ')
        dir = {'U': -1, 'D': 1, 'L': -1j, 'R': 1j}[dir]
        steps = int(steps)

        # Mark all the edges
        for _ in range(steps):
            edges.add(start_pos)
            start_pos += dir

    # Just for fun to test both
    if (res := flood_fill(edges)) == point_in_polygon(edges):
        return res


if __name__ == "__main__":
    print(part1(data))  # 50603
