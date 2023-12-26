from dotenv import load_dotenv
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'{{day}}.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def part1(data: list[str]) -> int:
    result = 0
    for line in data:
        pass
    return result


if __name__ == "__main__":
    print(part1(data))
