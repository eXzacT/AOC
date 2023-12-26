from src.part2 import part2, part2_binary_search, part2_quadratic_formula
from common import time_execution

input_str_part2 = '''Time:      7  15   30
Distance:  9  40  200'''


@time_execution
def test_part2():

    result = part2(input_str_part2.split('\n'))
    expected_result = 71503

    assert result == expected_result


@time_execution
def test_part2_binary_search():

    result = part2_binary_search(input_str_part2.split('\n'))
    expected_result = 71503

    assert result == expected_result


@time_execution
def test_part2_quadratic_formula():

    result = part2_quadratic_formula(input_str_part2.split('\n'))
    expected_result = 71503

    assert result == expected_result
