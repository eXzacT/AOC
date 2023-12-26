from src.part2 import part2
from common import time_execution

input_str_part2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
fiveight
7pqrstsixteen'''


@time_execution
def test_part2():

    result = part2(input_str_part2.split('\n'))
    expected_result = 339

    assert result == expected_result
