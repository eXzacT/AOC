from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-04.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]


def fully_intersects(elf1: str, elf2: str) -> bool:
    x1, y1 = map(int, elf1.split('-'))
    x2, y2 = map(int, elf2.split('-'))

    return x1 >= x2 and y1 <= y2 or x1 <= x2 and y1 >= y2


def part1(data: list[str]) -> int:
    return sum(fully_intersects(*line.split(',')) for line in data)


if __name__ == "__main__":
    print(part1(data))  # 567
