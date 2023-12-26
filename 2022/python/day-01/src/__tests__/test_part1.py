from src.part1 import part1, part1_v2
from common import time_execution

input_str_part1 = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''


@time_execution
def test_part1():
    assert part1(input_str_part1) == 24000


@time_execution
def test_part1_v2():
    assert part1_v2(input_str_part1) == 24000
