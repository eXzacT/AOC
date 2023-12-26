from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-01.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part2(data: str) -> int:
    return sum(sorted(sum(int(calories) for calories in elf_load.split('\n'))
                      for elf_load in data.split('\n\n'))[-3:])


def part2_v2(data: str) -> int:
    return sum(sorted(eval(elf_load.replace('\n', '+'))
                      for elf_load in data.split('\n\n'))[-3:])


if __name__ == "__main__":
    print(part2(data))  # 195292
    print(part2_v2(data))
