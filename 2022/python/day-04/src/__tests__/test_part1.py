from src.part1 import part1
from common import time_execution

input_part1 = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


@time_execution
def test_part1():
    assert part1(input_part1.split('\n')) == 2
