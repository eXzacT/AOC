from src.part1 import part1, part1_v2
from common import time_execution

input_part1 = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''


@time_execution
def test_part1():
    assert part1(input_part1) == 7


@time_execution
def test_part1_v2():
    assert part1_v2(input_part1) == 7
