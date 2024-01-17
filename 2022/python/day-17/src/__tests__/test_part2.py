from src.part2 import part2
from common import time_execution

input_part2 = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''


@time_execution
def test_part2():
    assert part2(input_part2) == 1514285714288
