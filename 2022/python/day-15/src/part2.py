from dotenv import load_dotenv
import os
import re
import z3

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-15.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


max_coords = 4000000 if __name__ == '__main__' else 20


def part2(data: str) -> int:
    '''4HbQ on reddit'''
    def ints(line): return map(int, re.findall(r'-?\d+', line))
    def dist(x1, y1, x2, y2): return abs(x2-x1)+abs(y2-y1)
    # List of sensor coords and their distance to the beacon
    data = [(x, y, dist(x, y, p, q))
            for x, y, p, q in map(ints, data.split('\n'))]

    def f(x1, y1, d1, x2, y2, d2) -> int:
        return ((x2+y2+d2+x1-y1-d1)//2, (x2+y2+d2-x1+y1+d1)//2+1)

    for X, Y in [f(*a, *b) for a in data for b in data]:
        if 0 < X < max_coords and 0 < Y < max_coords and all(dist(X, Y, x, y) > d for x, y, d in data):
            return X*4000000+Y


def part2_z3(data: str) -> int:
    def ints(line): return map(int, re.findall(r'-?\d+', line))
    def dist(x1, y1, x2, y2): return abs(x2-x1)+abs(y2-y1)
    # List of sensor coords and their distance to the beacon
    data = [(x1, y1, dist(x1, y1, x2, y2))
            for x1, y1, x2, y2 in map(ints, data.split('\n'))]

    s = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    s.add(0 <= x)
    s.add(x <= max_coords)
    s.add(0 <= y)
    s.add(y <= max_coords)

    def z3_abs(x): return z3.If(x >= 0, x, -x)

    for sx, sy, dist in data:
        s.add(z3_abs(sx - x) + z3_abs(sy - y) > dist)

    s.check()
    m = s.model()
    return m[x].as_long()*4000000 + m[y].as_long()


if __name__ == "__main__":
    print(part2(data))
    print(part2_z3(data))  # 10621647166538
