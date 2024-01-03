from src.part1 import part1
from common import time_execution

input_part1 = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

data = {complex(i, j): c for i, line in enumerate(input_part1.split('\n'))
        for j, c in enumerate(line.strip())}


@time_execution
def test_part1():
    assert part1(data) == 31
