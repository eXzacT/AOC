from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-24.txt'
with open(filename, 'r') as file:
    data = file.readlines()


def find_intersections(hailstones: list[list[int]], lo: int, hi: int) -> int:
    intersections = 0

    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            x1, y1, _, vx1, vy1, _ = hailstones[i]
            x2, y2, _, vx2, vy2, _ = hailstones[j]
            A = np.array([[vx1, -vx2], [vy1, -vy2]])
            b = np.array([x2 - x1, y2 - y1])

            if np.linalg.det(A) != 0:
                t = np.linalg.inv(A).dot(b)
                if t[0] >= 0 and t[1] >= 0:
                    intersection = (x1 + vx1*t[0], y1 + vy1*t[0])
                    if lo <= intersection[0] <= hi and lo <= intersection[1] <= hi:
                        intersections += 1

    return intersections


def part1(data: list[str], search_area: tuple[int, int]) -> int:
    data = [[int(i) for i in l.replace('@', ',').split(',')]
            for l in data]
    return find_intersections(data, *search_area)


if __name__ == "__main__":
    print(part1(data, (200000000000000, 400000000000000)))  # 17867
