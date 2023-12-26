from src.part2 import part2
from common import time_execution

input_part2 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


@time_execution
def test_part2():

    result = part2(input_part2)
    expected_result = 145

    assert result == expected_result
