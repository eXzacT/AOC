from src.part1 import part1
from common import time_execution

input_part1 = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 21

    assert result == expected_result
