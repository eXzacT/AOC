from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-04.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part1(cards: list[str]) -> int:
    scratch_cards_worth = 0
    for line in cards:

        left, right = line.split('|')
        left = left.split(':')[1]  # Skip Card X:

        winning_nums = re.findall(r'\d+', left)
        my_nums = re.findall(r'\d+', right)

        # Intersection of 2 sets(can't use & with lists)
        hits = len(set(winning_nums) & set(my_nums))
        if hits > 0:
            scratch_cards_worth += 1 << (hits-1)

    return scratch_cards_worth


if __name__ == '__main__':
    print(part1(file_contents))
