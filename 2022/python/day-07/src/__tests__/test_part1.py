from src.part1 import part1, part1_v2
from common import time_execution

input_part1 = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''


@time_execution
def test_part1():
    assert part1(input_part1.split('\n')) == 95437


@time_execution
def test_part1_v2():
    assert part1_v2(input_part1.split('\n')) == 95437
