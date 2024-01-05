from src.part2 import part2
from common import time_execution

input_part2 = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


@time_execution
def test_part2():
    assert part2(input_part2.split('\n')) == 93
