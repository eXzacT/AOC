from dotenv import load_dotenv
from functools import cmp_to_key
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-13.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def compare_pairs(l: list | int, r: list | int) -> int:
    match l, r:
        case int(), int(): return (l > r)-(l < r)
        case int(), list(): return compare_pairs([l], r)
        case list(), int(): return compare_pairs(l, [r])
        case list(), list():
            for comp_result in map(compare_pairs, l, r):
                if comp_result:  # Either left or right has a smaller element, return -1 or 1
                    return comp_result
            # No more elements in either or both sides, which is smaller?
            return compare_pairs(len(l), len(r))


def part2(data: str) -> int:
    packets = [eval(packet) for pairs in data.split(
        '\n\n') for packet in pairs.split('\n')]+[[2]]+[[6]]
    sorted_packets = sorted(packets, key=cmp_to_key(compare_pairs))
    return (sorted_packets.index([2])+1)*(sorted_packets.index([6])+1)


if __name__ == "__main__":
    print(part2(data))  # 19305
