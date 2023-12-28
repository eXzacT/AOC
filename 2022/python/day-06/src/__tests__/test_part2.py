from src.part2 import part2, part2_v2
from common import time_execution

input_part2 = '''bvwbjplbgvbhsrlpgdmjqwftvncz'''


@time_execution
def test_part2():
    assert part2(input_part2) == 23


@time_execution
def test_part2_v2():
    assert part2_v2(input_part2) == 23
