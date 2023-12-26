from src.part2 import part2
from common import time_execution

input_part2 = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


@time_execution
def test_part2():
    assert part2(input_part2) == 4
