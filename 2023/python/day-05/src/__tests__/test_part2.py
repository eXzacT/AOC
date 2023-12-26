from src.part2 import part2, part2_v2
from common import time_execution


input_str_part2 = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


@time_execution
def test_file_process_part2():

    result = part2(input_str_part2.split('\n'))
    expected_result = 46

    assert result == expected_result


@time_execution
def test_file_process_part2_v2():

    result = part2_v2(input_str_part2.split('\n'))
    expected_result = 46

    assert result == expected_result
