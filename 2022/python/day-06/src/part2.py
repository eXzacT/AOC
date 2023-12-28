from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-06.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part2(data: str) -> int:
    return [i for i in range(len(data)) if len(set(data[i:i+14])) == 14][0]+14


def part2_v2(data: str) -> int:
    i = 0
    while i < len(data):
        seen = 0
        for i in range(i+13, i-1, -1):  # Check 14 chars from the back
            # a=1,b=2,c=3... when we see c again we'll have b100 | b100, no difference
            if seen == (seen := seen | 1 << (ord(data[i])-97)):
                i += 1  # Next time check from the duplicate one
                break
        else:
            return i+14


if __name__ == "__main__":
    print(part2(data))  # 3534
    print(part2_v2(data))
