from dotenv import load_dotenv
import re
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-01.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def part2(data: list[str]) -> int:
    nums_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                 "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    sum_num = 0
    for line in data:
        regex = r'(?=(' + '|'.join(nums_dict.keys()) + '|\\d))'
        nums = re.findall(regex, line)
        first_num_str = nums_dict.get(nums[0], nums[0])
        last_num_str = nums_dict.get(nums[-1], nums[-1])

        sum_num += int(first_num_str+last_num_str)

    return sum_num


if __name__ == "__main__":
    print(part2(data))  # 55652
