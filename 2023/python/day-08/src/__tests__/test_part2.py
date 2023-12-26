from src.part2 import part2
from common import time_execution

input_part2 = '''LR

LLA = (LLB, XXX)
LLB = (XXX, LLZ)
LLZ = (LLB, XXX)
PPA = (PPB, XXX)
PPB = (PPC, PPC)
PPC = (PPZ, PPZ)
PPZ = (PPB, PPB)
XXX = (XXX, XXX)'''


@time_execution
def test_part2():

    result = part2(input_part2.split('\n'))
    expected_result = 6

    assert result == expected_result
