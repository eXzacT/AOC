from src.part1 import part1
from common import time_execution
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [('''broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a''', 32000000),

                          ('''broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output''', 11687500)])
@time_execution
def test_part1(test_input, expected):
    assert part1(test_input) == expected
