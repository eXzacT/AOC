from src.part2 import part2
from common import time_execution

input_part2 = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''


@time_execution
def test_part2():

    result = part2(input_part2.split('\n'))
    expected_result = 525152

    assert result == expected_result
