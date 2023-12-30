from src.part2 import part2
from common import time_execution

input_part2 = '''30373
25512
65332
33549
35390'''

data = {complex(i, j): int(c) for i, line in enumerate(
    input_part2.split('\n')) for j, c in enumerate(line)}


@time_execution
def test_part1():
    assert part2(data) == 8
