from src.part1 import part1
from common import time_execution
import pytest


@pytest.mark.parametrize(
    "input_part1, expected_result",
    [
        ("HASH", 52),
        ("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7", 1320),
    ],
)
@time_execution
def test_part1(input_part1, expected_result):
    assert part1(input_part1) == expected_result
