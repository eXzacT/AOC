from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-01.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    return max(sum(int(calories) for calories in elf_load.split('\n'))
               for elf_load in data.split('\n\n'))


def part1_v2(data: str) -> int:
    return max(eval(elf_load.replace('\n', '+'))
               for elf_load in data.split('\n\n'))


if __name__ == "__main__":
    print(part1(data))  # 66306
    print(part1_v2(data))
