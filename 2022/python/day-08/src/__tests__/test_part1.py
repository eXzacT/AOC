from src.part1 import part1
from common import time_execution

input_part1 = '''30373
25512
65332
33549
35390'''

data = {complex(i, j): (int(c), False) for i, line in enumerate(
    input_part1.split('\n')) for j, c in enumerate(line)}


@time_execution
def test_part1():
    assert part1(data) == 21
