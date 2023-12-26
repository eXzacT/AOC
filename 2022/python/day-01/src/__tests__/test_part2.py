from src.part2 import part2, part2_v2
from common import time_execution

input_str_part2 = '''1000
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
def test_part2():
    assert part2(input_str_part2) == 45000


@time_execution
def test_part2():
    assert part2_v2(input_str_part2) == 45000
