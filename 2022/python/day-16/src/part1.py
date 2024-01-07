from dotenv import load_dotenv
from collections import defaultdict
from itertools import product
from functools import cache
import os
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-16.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part1(data: str) -> int:
    '''4HbQ on reddit'''
    r = r'Valve (\w+) .*=(\d+); .* valves? (.*)'
    valves, valve_flow, dists = set(), dict(), defaultdict(lambda: float('inf'))

    for valve, flow_rate, conns in re.findall(r, data):
        valves.add(valve)
        if flow_rate != '0':
            valve_flow[valve] = int(flow_rate)
        for conn in conns.split(', '):
            # The connections we know about have a distance of 1
            dists[conn, valve] = 1

    # Find all the unknown distances
    for k, i, j in product(valves, valves, valves):    # floyd-warshall
        if i == j or j == k or i == k:
            continue
        dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])

    @cache
    # Frozen set so we can cache, also by doing f-{v} we're removing that valve so we can't turn it again
    def search(t: int, f=frozenset(valve_flow), start='AA'):
        return max([valve_flow[v] * (t-dists[start, v]-1) + search(t-dists[start, v]-1, f-{v}, start=v)
                    # If we have time to visit it, +[0] in case it's an empty list so max doesn't complain
                    for v in f if dists[start, v] < t] + [0])

    return search(30)


if __name__ == "__main__":
    print(part1(data))  # 1659
