from dotenv import load_dotenv
import re
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-15.txt'
with open(filename, 'r') as file:
    data = file.read().strip()

goal_row = 2000000 if __name__ == '__main__' else 10


def part1(data: str) -> int:
    digits = list(map(int, re.findall(r'-?\d+', data)))
    sensor_beacon_pairs = [(digits[i], digits[i+1], digits[i+2], digits[i+3])
                           for i in range(0, len(digits), 4)]

    min_pos = float('+inf')
    max_pos = float('-inf')

    for sensor_x, sensor_y, beacon_x, beacon_y in sensor_beacon_pairs:
        distance_to_beacon = abs(sensor_x - beacon_x) + \
            abs(sensor_y - beacon_y)
        dist_to_goal_row = abs(sensor_y - goal_row)

        if dist_to_goal_row > distance_to_beacon:  # Can't reach the row anyway
            continue

        # We have this many steps left in either direction on the row
        dist_left = distance_to_beacon - dist_to_goal_row
        if (res := sensor_x + dist_left) > max_pos:
            max_pos = res
        if (res := sensor_x - dist_left) < min_pos:
            min_pos = res

    # Not sure if this will work for every input, but it seems to be a contiguous range
    return max_pos-min_pos

    # Merge overlapping or continuous ranges
    ranges.sort()
    merged_ranges = [ranges[0]]
    for current in ranges:
        previous = merged_ranges[-1]
        if current[0] <= previous[1] + 1:
            merged_ranges[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged_ranges.append(current)

    # Calculate the length of all ranges
    return sum(max_pos - min_pos + 1 for min_pos, max_pos in merged_ranges)-1


def part1_v2(data: str) -> int:
    '''4HbQ on reddit'''
    def ints(line): return map(int, re.findall(r'-?\d+', line))
    def dist(x1, y1, x2, y2): return abs(x2-x1)+abs(y2-y1)
    # List of sensor coords and their distance to the beacon
    data = [(x, y, dist(x, y, p, q))
            for x, y, p, q in map(ints, data.split('\n'))]

    return (max(x - abs(goal_row-y) + d for x, y, d in data)
            - min(x + abs(goal_row-y) - d for x, y, d in data))


if __name__ == "__main__":
    print(part1(data))  # 5461729
    print(part1_v2(data))
