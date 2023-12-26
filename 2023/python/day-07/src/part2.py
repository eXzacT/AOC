from dotenv import load_dotenv
import os
import bisect

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-07.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


class CardHand():
    def __repr__(self) -> str:
        return f"Hand: {self.hand}, Rank: {self.rank}, Bet:{self.bet}"

    def __init__(self, hand: str, bet: int = 0) -> None:
        self.hand = hand
        self.rank = self.assign_rank()
        self.bet = bet

    def __gt__(self, other) -> bool:
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False
        # If they have same rank then compare 1 by 1
        if self.rank == other.rank:
            return self.compare_by_char(other.hand)

    def assign_rank(self) -> int:

        hand = self.hand
        # Extract number of jokers and remove occurences from the string
        jokers = hand.count('J')
        hand = hand.replace('J', '')
        if hand == '':  # Hand full of jokers edge case
            return 7

        duplicates = sorted(
            map(hand.count, set(hand)), reverse=True)

        # Add jokers to the max count(which is first)
        duplicates[0] += jokers

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

        card_value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}

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


def part2(input_list: list[str]) -> int:
    hands: list[CardHand] = []
    # Adding hands by their strength to the array
    for line in input_list:
        hand, bet = line.split(' ')
        hand = CardHand(hand, int(bet))
        # implemented __gt__ on CardHand so this works
        bisect.insort(hands, hand)
        # print(hand)

    winnings = 0
    for rank, hand in enumerate(hands, start=1):
        winnings += rank*hand.bet
    return winnings


if __name__ == "__main__":
    print(part2(file_contents))  # 248256639
