from src.part2 import part2
from common import time_execution

input_part2 = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''


@time_execution
def test_part2():
    assert part2(input_part2.split('\n')) == 47
