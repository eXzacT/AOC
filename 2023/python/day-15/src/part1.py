from dotenv import load_dotenv
import os
from operator import add
from functools import reduce

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-15.txt'
with open(filename, 'r') as file:
    file_contents = file.read().strip()


def part1(input_str: str) -> int:
    return reduce(add,
                  [reduce(lambda carry, c: (carry+ord(c))*17 % 256, step, 0)
                   for step in input_str.split(',')], 0)


if __name__ == "__main__":
    print(part1(file_contents))  # 511257
