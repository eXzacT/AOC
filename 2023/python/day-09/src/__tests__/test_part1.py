from src.part1 import part1
from common import time_execution

input_part1 = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 114

    assert result == expected_result
