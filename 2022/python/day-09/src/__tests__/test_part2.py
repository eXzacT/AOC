from src.part2 import part2
from common import time_execution

input_part2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''


@time_execution
def test_part2():
    assert part2(input_part2.split('\n')) == 36
