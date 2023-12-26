from src.part2 import part2
from common import time_execution

input_part2 = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


@time_execution
def test_part2():

    result = part2(input_part2.split('\n'))
    expected_result = 2

    assert result == expected_result
