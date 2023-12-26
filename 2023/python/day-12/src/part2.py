from dotenv import load_dotenv
from functools import cache
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-12.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part2(input_list: list[str]) -> int:
    total_arrangements = 0

    for line in input_list:
        chars, digits = line.split(' ')
        chars, digits = (chars+'?')*5, eval(digits)*5

        @cache
        def dp(char_idx: int, digit_idx: int, arrangements=0):
            if char_idx == len(chars):
                return digit_idx == len(digits)

            if chars[char_idx] in '.?':
                arrangements += dp(char_idx+1, digit_idx)
            try:
                q = char_idx+digits[digit_idx]
                if chars[char_idx] in '#?' and '.' not in chars[char_idx:q] and '#' not in chars[q]:
                    arrangements += dp(q+1, digit_idx+1)
            except IndexError:
                pass

            return arrangements

        arrangements = dp(0, 0)
        total_arrangements += arrangements

    return total_arrangements


if __name__ == "__main__":
    print(part2(file_contents))  # 7139671893722
