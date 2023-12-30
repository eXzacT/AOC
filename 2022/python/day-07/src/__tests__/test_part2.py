from src.part2 import part2, part2_v2
from common import time_execution

input_part2 = '''$ cd /
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
def test_part2():
    assert part2(input_part2.split('\n')) == 24933642


@time_execution
def test_part2_v2():
    assert part2_v2(input_part2.split('\n')) == 24933642
