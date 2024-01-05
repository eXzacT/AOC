from dotenv import load_dotenv
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


def part1(data: str) -> int:
    # Sum all the indexes of pairs where the first one was smaller than the other one
    return sum(i for i, pairs in enumerate(data.split('\n\n'), start=1)
               if compare_pairs(*map(eval, pairs.split('\n'))) == -1)


if __name__ == "__main__":
    print(part1(data))  # 6484
