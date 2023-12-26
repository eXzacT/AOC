from src.part1 import part1, part1_v2
from common import time_execution

input_part1 = '''A Y
B X
C Z'''


@time_execution
def test_part1():
    assert part1(input_part1) == 15


@time_execution
def test_part1_v2():
    assert part1_v2(input_part1) == 15
