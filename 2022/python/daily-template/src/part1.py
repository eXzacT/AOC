from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'{{day}}.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    result = 0

    return result


if __name__ == "__main__":
    print(part1(data))
