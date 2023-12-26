from dotenv import load_dotenv
from functools import reduce
from operator import add
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-09.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part1(input_list: list[str]) -> int:
    sum_last = 0
    for line in input_list:
        save_last_num_in_seq: list[int] = []

        # Extract the sequences, convert to numbers and save last number
        seq = line.split(' ')
        seq = [int(char) for char in seq]
        save_last_num_in_seq.append(seq[-1])

        # Keep decreasing the sequence until it's all zeros
        # Also save the last number during each step
        while seq.count(0) != len(seq):
            seq = [seq[idx]-seq[idx-1]
                   for idx in range(1, len(seq))]
            save_last_num_in_seq.append(seq[-1])

        # Find out what the next number in the sequence should be and add it
        sum_last += reduce(add, reversed(save_last_num_in_seq))

    return sum_last


if __name__ == "__main__":
    print(part1(file_contents))
