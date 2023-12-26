from dotenv import load_dotenv
import os
import re


load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-02.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part2(data: str) -> int:
    substitutions = {'A X': '0+3', 'A Y': '3+1', 'A Z': '6+2',
                     'B X': '0+1', 'B Y': '3+2', 'B Z': '6+3',
                     'C X': '0+2', 'C Y': '3+3', 'C Z': '6+1'}

    data = re.sub('|'.join(substitutions.keys()),
                  lambda match: substitutions[match[0]], data)

    return sum(map(eval, data.split('\n')))


def part2_v2(data: str) -> int:
    ordered_scores = ['', 'B X', 'C X', 'A X',
                      'A Y', 'B Y', 'C Y',
                      'C Z', 'A Z', 'B Z']

    return sum(map(ordered_scores.index, data.split('\n')))


if __name__ == "__main__":
    print(part2(data))  # 13448
    print(part2_v2(data))
