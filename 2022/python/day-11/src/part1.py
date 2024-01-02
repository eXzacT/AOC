from dotenv import load_dotenv
from math import prod
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-11.txt'
with open(filename, 'r') as file:
    data = file.read().strip().split('\n\n')


class Monkey:
    def __init__(self, data: str):
        lines = data.split('\n')
        self.items = lines[1].split(': ')[1].split(', ')
        self.operation = lines[2].split('= ')[1]
        self.divisor = int(lines[3].split(' ')[-1])
        self.true_id = int(lines[4].split(' ')[-1])
        self.false_id = int(lines[5].split(' ')[-1])
        self.inspect_count = 0

    def __repr__(self) -> str:
        return f'<Monkey {id(self)} has items {self.items}, inspecting: {self.operation} divisble by {self.divisor} ? {self.true_id}:{self.false_id} >\n'

    def throw(self, monkeys: list['Monkey']) -> None:
        for _ in range(len(self.items)):
            item = eval(self.operation.replace('old', str(self.items.pop())))
            item //= 3
            self.inspect_count += 1

            if item % self.divisor == 0:
                monkeys[self.true_id].items.append(item)
            else:
                monkeys[self.false_id].items.append(item)


def part1(data: list[str]) -> int:
    monkeys: list[Monkey] = [*map(Monkey, data)]
    for _ in range(20):
        for monkey in monkeys:
            monkey.throw(monkeys)  # Pass a reference so items can be moved

    return prod(sorted(m.inspect_count for m in monkeys)[-2:])


if __name__ == "__main__":
    print(part1(data))  # 110264
