from dotenv import load_dotenv
from collections import deque, defaultdict
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-05.txt'
with open(filename, 'r') as file:
    data = file.read()


def part2(data: list[str]) -> str:
    stacks = defaultdict(deque)

    stack_data, instructions = data.split('\n\n')
    idx = 0
    for i in range(1, len(stack_data), 4):
        c = stack_data[i]
        idx += 1
        if stack_data[i-2] == '\n':
            idx = 1  # In a new line, reset stack index
        if c != ' ' and not c.isdigit():
            stacks[idx].appendleft(c)

    for instruction in instructions.split('\n'):
        quantity, _from, _to = map(int, instruction.split()[1::2])
        popped_list = []
        for _ in range(quantity):
            popped_list.append(stacks[_from].pop())

        stacks[_to].extend(reversed(popped_list))

    return ''.join([stack.pop() for _, stack in sorted(stacks.items())])


def part2_v2(data: list[str]) -> str:
    stack_data, instructions = data.split('\n\n')

    stacks = [[]]+["".join(c).strip()
                   for c in zip(*stack_data.split('\n'))][1::4]

    for instruction in instructions.split('\n'):
        quantity, _from, _to = map(int, instruction.split()[1::2])
        stacks[_to] = stacks[_from][:quantity]+stacks[_to]
        stacks[_from] = stacks[_from][quantity:]

    return ''.join([stack[0] for stack in stacks if stack])


if __name__ == "__main__":
    print(part2(data))  # BNTZFPMMW
    print(part2_v2(data))
