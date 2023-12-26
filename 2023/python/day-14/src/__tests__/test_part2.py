from src.part2 import part2
from common import time_execution
import pytest

input_part2 = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


@pytest.mark.parametrize("cycles,expected", [
    (1, 87),
    (2, 69),
    (120, 63),
    (1_000_000_000, 64)
])
@time_execution
def test_part2(cycles, expected):

    assert part2(input_part2.split('\n'), cycles=cycles) == expected
