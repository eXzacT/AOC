from dotenv import load_dotenv
import os
import z3

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-24.txt'
with open(filename, 'r') as file:
    data = file.readlines()


def part2(data: list[str]) -> int:
    # 4HbQ on reddit
    data = [[int(i) for i in l.replace('@', ',').split(',')]
            for l in data]
    rock = z3.RealVector('r', 6)
    time = z3.RealVector('t', 3)

    s = z3.Solver()
    s.add(*[rock[d] + rock[d+3] * t == hail[d] + hail[d+3] * t
            for t, hail in zip(time, data) for d in range(3)])
    s.check()

    return (s.model().eval(sum(rock[:3])))


if __name__ == "__main__":
    print(part2(data))  # 557743507346379
