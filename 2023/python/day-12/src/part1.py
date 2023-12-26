from dotenv import load_dotenv
from itertools import combinations
import os
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-12.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part1(input_list: list[str]) -> int:
    arrangements = 0

    for line in input_list:
        chars, digits = line.split(' ')
        digits = list(eval(digits))

        total_hashes = sum(digits)
        hash_count = chars.count('#')
        to_change = total_hashes-hash_count

        question_mark_positions = [i for i, c in enumerate(chars) if c == '?']

        for combination in combinations(question_mark_positions, to_change):
            new_line = ''.join('#' if idx in combination else chars[idx]
                               for idx in range(len(chars)))
            hashes = re.findall(r'#+', new_line)
            if [len(hash_group) for hash_group in hashes] == digits:
                arrangements += 1

    return arrangements


if __name__ == "__main__":
    print(part1(file_contents))
