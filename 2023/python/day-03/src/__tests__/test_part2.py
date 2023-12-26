from src.part2 import part2
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
def test_part2():

    result = part2(schematic.split('\n'))
    expected_result = 467835

    assert result == expected_result
