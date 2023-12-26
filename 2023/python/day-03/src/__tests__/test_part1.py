from src.part1 import part1, part1_v2, part1_and_part2
from common import time_execution

schematic = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''


@time_execution
def test_part1():

    result = part1(schematic.split('\n'))
    expected_result = 4361

    assert result == expected_result


@time_execution
def test_part1_v2():

    result = part1_v2(schematic.split('\n'))
    expected_result = 4361

    assert result == expected_result


@time_execution
def test_part1_and_part2():

    results = part1_and_part2(schematic.split('\n'))
    expected_results = 4361, 467835

    assert results == expected_results
