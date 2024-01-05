from src.part1 import part1
from common import time_execution

input_part1 = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


@time_execution
def test_part1():
    assert part1(input_part1.split('\n')) == 24
