from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-14.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part1(input_list: list[str]) -> int:
    boundaries: list[tuple[int, int]] = []
    height = len(input_list)
    result = 0

    def replace_or_insert(locations: list[tuple[int, int]], rock_type: str) -> int:
        '''
        Update all previous boundaries if they existed, otherwise add the new one
        Also increment result based on which row we moved the rock to
        '''
        nonlocal result

        for row1, col1 in locations:
            for i, (row2, col2) in enumerate(boundaries):
                if col1 == col2:
                    if rock_type == '#':  # Update boundary row index
                        boundaries[i] = (row1, col2)
                    else:  # Stone rolled over on top of that position
                        # Position is +1 but value is -1
                        result += height-row2-1
                        boundaries[i] = (row2 + 1, col2)
                    break

            else:
                if rock_type == '#':  # Can't move so save location as is
                    boundaries.append((row1, col1))
                else:  # Move all the way to bottom since nothing is blocking
                    boundaries.append((0, col1))
                    result += height

    for row, line in enumerate(input_list):
        rounded = [(row, col) for col, c in enumerate(
            line) if c == 'O']
        cubic = [(row, col) for col, c in enumerate(
            line) if c == '#']

        replace_or_insert(rounded, 'O')
        replace_or_insert(cubic, '#')

    return result


if __name__ == "__main__":
    print(part1(file_contents))  # 108813
