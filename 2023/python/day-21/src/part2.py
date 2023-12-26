from dotenv import load_dotenv
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-21.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): c for i, r in enumerate(file.readlines())
            for j, c in enumerate(r) if c in '.S'}

WIDTH, HEIGHT = (131, 131)


def part2(data: dict[complex, str], steps: int):

    points = []
    stack = {pos for pos in data if data[pos] == 'S'}
    # Adjusts out-of-bounds positions by overlaying the map onto another.
    def cmod(x): return complex(x.real % HEIGHT, x.imag % WIDTH)

    for s in range(3 * WIDTH):
        if s % WIDTH == WIDTH//2:  # Reached the mid point
            points.append(len(stack))
            if len(points) == 3:  # Break early
                break

        stack = {pos+d for d in {1, -1, 1j, -1j}
                 for pos in stack if cmod(pos+d) in data}

    # Quadratic formula
    def f(n, a, b, c): return a+n*(b-a+(n-1)*(c-b-b+a)//2)
    return (f(steps // WIDTH, *points))


if __name__ == "__main__":
    print(part2(data, 26501365))  # 621944727930768
