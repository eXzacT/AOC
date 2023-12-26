from src.part1 import part1
from common import time_execution

input_part1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 2

    assert result == expected_result
