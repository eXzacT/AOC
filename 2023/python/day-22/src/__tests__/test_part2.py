import re
from src.part2 import part2
from common import time_execution

input_part1 = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''

data = re.findall(r'\d+', input_part1)
data = [int(num) for num in data]

# Group every six numbers together, and sort based on last number
data = [data[i:i+6] for i in range(0, len(data), 6)]
data.sort(key=lambda x: x[-1])


@time_execution
def test_part2():
    assert part2(data) == 7
