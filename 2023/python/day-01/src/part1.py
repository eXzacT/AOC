# Day 1: Trebuchet?!
from dotenv import load_dotenv
import re
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-01.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def part1(data: list[str]) -> int:
    result = 0
    for line in data:
        numbers = re.findall('[0-9]', line)
        result += int(numbers[0]+numbers[-1])

    return result


if __name__ == "__main__":
    print(part1(data))  # 56108
