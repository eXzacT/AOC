from src.part1 import part1
from common import time_execution

input_part1 = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

data = {complex(i, j): c if c != '.' else 0 for i, row in enumerate(input_part1.split('\n'))
        for j, c in enumerate(row)}


@time_execution
def test_part1():
    assert part1(data, 6) == 16
