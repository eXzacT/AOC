from src.part1 import part1
from common import time_execution

input_part1 = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 8

    assert result == expected_result
