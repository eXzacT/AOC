from src.part2 import part2
from common import time_execution

input_part2 = '''..##..###
##..##.#.
#######..
......#..
..##...##
#.##.##.#
......###'''


@time_execution
def test_part2():

    result = part2(input_part2.split('\n'))
    expected_result = 1

    assert result == expected_result
