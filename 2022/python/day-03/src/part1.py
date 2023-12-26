from dotenv import load_dotenv
import os
import re
import string

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-03.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    scoring = string.ascii_letters  # String from a-zA-Z
    return (sum(scoring.index(  # Score as follows a=1, b=2,...A=27, B=28...
        # Find a character that repeats in both parts of a line split by a space
        re.findall(r"(\w).* .*\1", line[:len(line)//2]+" "+line[len(line)//2:])
            [0])+1
        for line in data.split('\n')))


if __name__ == "__main__":
    print(part1(data))  # 8139
