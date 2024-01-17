from src.part1 import part1
from common import time_execution

input_part1 = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''


@time_execution
def test_part1():
    assert part1(input_part1) == 3068
