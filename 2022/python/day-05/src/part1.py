from dotenv import load_dotenv
from collections import deque, defaultdict
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-05.txt'
with open(filename, 'r') as file:
    data = file.read()


def part1(data: list[str]) -> str:
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
        for _ in range(quantity):
            popped = stacks[_from].pop()
            stacks[_to].append(popped)

    return ''.join([stack.pop() for _, stack in sorted(stacks.items())])


def part1_v2(data: list[str]) -> str:
    stack_data, instructions = data.split('\n\n')
    stacks = [[]]+[''.join(c).strip()
                   for c in zip(*stack_data.split('\n'))][1::4]

    for instruction in instructions.split('\n'):
        quantity, _from, _to = map(int, instruction.split()[1::2])
        stacks[_to] = stacks[_from][:quantity][::-1]+stacks[_to]
        stacks[_from] = stacks[_from][quantity:]

    return ''.join([stack[0] for stack in stacks if stack])


if __name__ == "__main__":
    print(part1(data))  # PSNRGBTFT
    print(part1_v2(data))
