from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-04.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part2(cards: list[str]) -> int:
    total_cards = 0
    # Add every card in the dictionary once
    copies = {num: 1 for num in range(1, len(cards)+1)}
    for line in cards:

        left, right = line.split('|')

        winning_nums = re.findall(r'\d+', left)
        card_number = int(winning_nums.pop(0))
        my_nums = re.findall(r'\d+', right)

        # Intersection of 2 sets(can't use & with lists)
        hits = len(set(winning_nums) & set(my_nums))

        self_copy_count = copies[card_number]
        total_cards += self_copy_count

        if hits > 0:
            # For next *hits* cards update their count in the dictionary
            for card_num in range(card_number+1, card_number+hits+1):
                copies[card_num] += self_copy_count

    return total_cards


if __name__ == '__main__':
    print(part2(file_contents))
