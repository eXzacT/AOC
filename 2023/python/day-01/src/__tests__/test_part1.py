from src.part1 import part1
from common import time_execution

input_str_part1 = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''


@time_execution
def test_part1():

    result = part1(input_str_part1.split('\n'))
    expected_result = 142

    assert result == expected_result
