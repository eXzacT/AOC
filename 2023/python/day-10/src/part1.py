from dotenv import load_dotenv
from collections import deque
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-10.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]

connecting_pipes_dict = {'|': ['N', 'S'], '-': ['E', 'W'],
                         'L': ['N', 'E'], 'J': ['W', 'N'],
                         '7': ['W', 'S'], 'F': ['E', 'S']}


def part1(input_list: list[str]) -> int:

    pipe_locations: set[tuple(int, int)] = set()
    queue = deque()
    rows = len(input_list)
    cols = len(input_list[0])

    def add_if_connecting(direction_from: str, row: int, col: int) -> None:
        # Out of bounds
        if row >= rows or col >= cols or row < 0 or col < 0:
            return
        pipe = input_list[row][col]

        if pipe == '.':
            return

        connects_directions = connecting_pipes_dict.get(pipe, [])
        # Pipe and where we're coming from is compatible
        if direction_from in connects_directions:
            loc = (row, col)
            # Haven't seen this pipe before
            if loc not in pipe_locations:
                # Find out where the pipe leads
                direction_to = next(
                    direction for direction in connects_directions if direction != direction_from)
                pipe_locations.add(loc)
                queue.append((direction_to, loc))

    for row, line in enumerate(input_list):
        col = line.find('S')
        if col != -1:  # Found the start pipe
            # This new position is EAST of current start position
            add_if_connecting('E', row, col-1)
            # This new position is WEST of current start position
            add_if_connecting('W', row, col+1)
            # This new position is SOUTH of current start position
            add_if_connecting('S', row-1, col)
            # This new position is NORTH of current start position
            add_if_connecting('N', row+1, col)
            break

    while queue:
        # Unlike start pipe we know where to go
        going_to, (row, col) = queue.popleft()
        if going_to == 'N':
            row -= 1
            going_from = 'S'
        elif going_to == 'S':
            row += 1
            going_from = 'N'
        elif going_to == 'E':
            col += 1
            going_from = 'W'
        else:
            col -= 1
            going_from = 'E'
        add_if_connecting(going_from, row, col)

    return (len(pipe_locations)+1)//2


if __name__ == "__main__":
    print(part1(file_contents))  # 6701
