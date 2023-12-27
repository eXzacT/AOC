from src.part1 import part1, part1_v2
from common import time_execution

input_part1 = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


@time_execution
def test_part1():
    assert part1(input_part1) == "CMZ"


@time_execution
def test_part1_v2():
    assert part1_v2(input_part1) == "CMZ"
