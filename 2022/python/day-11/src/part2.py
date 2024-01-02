from dotenv import load_dotenv
import os
import math

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

    def throw(self, monkeys: list['Monkey'], lcm: int) -> None:
        for _ in range(len(self.items)):
            item = eval(self.operation.replace('old', str(self.items.pop())))
            item %= lcm
            self.inspect_count += 1

            if item % self.divisor == 0:
                monkeys[self.true_id].items.append(item)
            else:
                monkeys[self.false_id].items.append(item)


def part2(data: list[str]) -> int:
    monkeys: list[Monkey] = [*map(Monkey, data)]
    lcm = math.prod(m.divisor for m in monkeys)

    for _ in range(10_000):
        for monkey in monkeys:
            # Pass a reference so items can be moved
            monkey.throw(monkeys, lcm)

    return math.prod(sorted(m.inspect_count for m in monkeys)[-2:])


if __name__ == "__main__":
    print(part2(data))  # 23612457316
