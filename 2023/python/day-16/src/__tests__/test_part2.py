from src.part2 import part2
from common import time_execution

input_part1 = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

input_part2 = {complex(i, j): c for i, row in enumerate(input_part1.split('\n'))
               for j, c in enumerate(row)}


@time_execution
def test_part1():
    assert part2(input_part2) == 51
