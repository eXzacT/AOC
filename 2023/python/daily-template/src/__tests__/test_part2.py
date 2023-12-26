from src.part2 import part2
from common import time_execution

input_part2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''


@time_execution
def test_part2():
    assert part2(input_part2.split('\n')) == 281
