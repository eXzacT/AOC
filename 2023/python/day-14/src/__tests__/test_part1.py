from src.part1 import part1
from common import time_execution

input_part1 = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 136

    assert result == expected_result
