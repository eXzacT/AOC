from src.part2 import part2, part2_v2
from common import time_execution

input_part2 = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


@time_execution
def test_part2():
    assert part2(input_part2) == 70


@time_execution
def test_part2_v2():
    assert part2_v2(input_part2) == 70
