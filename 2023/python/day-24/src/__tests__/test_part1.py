from src.part1 import part1
from common import time_execution

input_part1 = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''


@time_execution
def test_part1():
    assert part1(input_part1.split('\n'), (7, 27)) == 2
