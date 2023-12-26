from dotenv import load_dotenv
import os
# import numpy as np
import bisect

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-07.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


class CardHand():
    def __repr__(self) -> str:
        return f"Hand: {self.hand}, Type: {self.type}, Bet:{self.bet}"

    def __init__(self, hand: str, bet: int = 0) -> None:
        self.hand = hand
        self.type = self.assign_type()
        self.bet = bet

    def __gt__(self, other) -> bool:
        if self.type > other.type:
            return True
        elif self.type < other.type:
            return False
        # If they have same type then compare 1 by 1
        if self.type == other.type:
            return self.compare_by_char(other.hand)

    def assign_type(self) -> int:
        duplicates = sorted(map(self.hand.count, set(self.hand)), reverse=True)
        hand_ranks = {
            (5,): 7,  # Five of a kind
            (4, 1): 6,  # Four of a kind
            (3, 2): 5,  # Full house
            (3, 1, 1): 4,  # Three of a kind
            (2, 2, 1): 3,  # Two pairs
            (2, 1, 1, 1): 2,  # One pair
        }
        return hand_ranks.get(tuple(duplicates), 1)  # Default High card

    # Compare each character numerical strength
    def compare_by_char(self, other_hand: str) -> bool:
        card_value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

        for idx in range(len(other_hand)):
            self_char = self.hand[idx]
            other_char = other_hand[idx]

            try:
                self_char = card_value_dict[self_char]
            except KeyError:
                self_char = int(self_char)
            try:
                other_char = card_value_dict[other_char]
            except KeyError:
                other_char = int(other_char)

            if self_char == other_char:
                continue
            return self_char > other_char


def part1(input_list: list[str]) -> int:
    hands = []
    for line in input_list:
        hand, bet = line.split(' ')
        hand = CardHand(hand, int(bet))
        bisect.insort(hands, hand)
        print(hand)

    # Walk the array and find the result
    winnings = 0
    for idx, hand in enumerate(hands, 1):
        winnings += idx*hand.bet
    return winnings


if __name__ == "__main__":
    print(part1(file_contents))  # 246424613
