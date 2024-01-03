from src.part2 import part2
from common import time_execution

input_part2 = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

data = {complex(i, j): c for i, line in enumerate(input_part2.split('\n'))
        for j, c in enumerate(line.strip())}


@time_execution
def test_part2():
    assert part2(data) == 29
