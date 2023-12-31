from src.part1 import part1
from common import time_execution

input_part1 = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''


@time_execution
def test_part1():
    assert part1(input_part1.split('\n')) == 13
