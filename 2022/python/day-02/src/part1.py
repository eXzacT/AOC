from dotenv import load_dotenv
import os
import re


load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-02.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    substitutions = {'A X': '3+1', 'A Y': '6+2', 'A Z': '0+3',
                     'B X': '0+1', 'B Y': '3+2', 'B Z': '6+3',
                     'C X': '6+1', 'C Y': '0+2', 'C Z': '3+3'}

    data = re.sub('|'.join(substitutions.keys()),
                  lambda match: substitutions[match[0]], data)

    return sum(map(eval, data.split('\n')))


def part1_v2(data: str) -> int:
    ordered_scores = ['', 'B X', 'C Y', 'A Z',
                      'A X', 'B Y', 'C Z', 'C X', 'A Y', 'B Z']

    return sum(map(ordered_scores.index, data.split('\n')))


if __name__ == "__main__":
    print(part1(data))  # 13924
    print(part1_v2(data))
