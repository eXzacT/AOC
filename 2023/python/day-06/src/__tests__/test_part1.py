from src.part1 import part1
from common import time_execution

input_str_part1 = '''Time:      7  15   30
Distance:  9  40  200'''


@time_execution
def test_file_process_part1():

    result = part1(input_str_part1.split('\n'))
    expected_result = 288

    assert result == expected_result
