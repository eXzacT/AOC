from src.part2 import part2, part2_v2
from common import time_execution

input_part2 = '''A Y
B X
C Z'''


@time_execution
def test_part2():
    assert part2(input_part2) == 12


@time_execution
def test_part2_v2():
    assert part2_v2(input_part2) == 12
