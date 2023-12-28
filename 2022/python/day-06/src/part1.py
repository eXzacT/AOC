from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-06.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    return [i for i in range(len(data)) if len(set(data[i:i+4])) == 4][0]+4


def part1_v2(data: str) -> int:
    i = 0
    while i < len(data):
        seen = 0
        for i in range(i+3, i-1, -1):
            if seen == (seen := seen | 1 << (ord(data[i])-97)):
                i += 1
                break
        else:
            return i+4


if __name__ == "__main__":
    print(part1(data))  # 1093
    print(part1_v2(data))
