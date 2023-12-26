from src.part1 import part1, CardHand
from common import time_execution
import pytest

input_part1 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''


@pytest.mark.parametrize("hand1,hand2,expected", [
    ('32T3K', 'T55J5', False),  # bool represents whether hand1 is stronger
    ('32T3K', 'KK677', False),
    ('32T3K', 'KTJJT', False),
    ('32T3K', 'QQQJA', False),
    ('32T3K', '32Q3K', False),
    ('T55J5', 'KK677', True),
    ('T55J5', 'KTJJT', True),
    ('T55J5', 'QQQJA', False),
    ('KK677', 'KTJJT', True),
    ('KK677', 'QQQJA', False),
    ('KTJJT', 'QQQJA', False),
])
def test_card_comparison(hand1: str, hand2: str, expected: bool):
    hand1 = CardHand(hand1)
    hand2 = CardHand(hand2)
    assert (hand1 > hand2) == expected


@time_execution
def test_part1():

    result = part1(input_part1.split('\n'))
    expected_result = 6440

    assert result == expected_result
