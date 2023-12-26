from dotenv import load_dotenv
import os
from functools import reduce

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-09.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def part2(input_list: list[str]) -> int:
    sum_first = 0
    for line in input_list:
        save_first_num_in_seq: list[int] = []

        # Extract the sequences, convert to numbers and save first number
        seq = line.split(' ')
        seq = [int(char) for char in seq]
        save_first_num_in_seq.append(seq[0])

        # Keep decreasing the sequence until it's all zeros
        # Also save the first number during each step
        while seq.count(0) != len(seq):
            seq = [seq[idx]-seq[idx-1]
                   for idx in range(1, len(seq))]  # 1 to len to have 1 element less
            save_first_num_in_seq.append(seq[0])

        # Subtract carry from number until the list is exhausted
        sum_first += reduce(lambda carry, num: num-carry,
                            reversed(save_first_num_in_seq))

    return sum_first


if __name__ == "__main__":
    print(part2(file_contents))  # 1140
