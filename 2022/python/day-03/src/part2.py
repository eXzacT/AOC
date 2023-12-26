from dotenv import load_dotenv
from collections import Counter
import os
import re
import string

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-03.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part2(data: str) -> int:
    badges_sum = 0
    scoring = string.ascii_letters  # String from a-zA-Z
    for i, line in enumerate(data.split('\n'), 1):
        if i % 3 == 1:  # create a counter every 3 loops starting from 1st
            counter = Counter(line)
        else:  # Get only the characters that repeat both counters
            counter = Counter(line) & counter

        # If we processed 3 lines, pop the remaining character and score it
        if i % 3 == 0:
            badge, _ = counter.popitem()
            badges_sum += scoring.index(badge)+1

    return badges_sum


def part2_v2(data: str) -> int:
    scoring = string.ascii_letters
    return sum(
        scoring.index(set.intersection(*[set(lines)
                      for lines in block_of_3_lines]).pop())+1
        for block_of_3_lines in zip(*[iter(data.split('\n'))]*3))


if __name__ == "__main__":
    print(part2(data))  # 2668
    print(part2_v2(data))
