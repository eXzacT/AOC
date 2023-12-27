from src.part2 import part2, part2_v2
from common import time_execution

input_part2 = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


@time_execution
def test_part2():
    assert part2(input_part2) == "MCD"


@time_execution
def test_part2_v2():
    assert part2_v2(input_part2) == "MCD"
