from src.part2 import part2
from common import time_execution

input_part2 = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

data = {complex(i, j): int(c) for i, row in enumerate(input_part2.split('\n'))
        for j, c in enumerate(row.strip())}


@time_execution
def test_part2():
    assert part2(data) == 94
