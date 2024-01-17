from dotenv import load_dotenv
import os
from collections import defaultdict
from itertools import permutations
from functools import cache
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-16.txt'
with open(filename, 'r') as file:
    data = file.read().strip()


def part2(data: str) -> int:
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
    for k, i, j in permutations(valves, 3):    # floyd-warshall
        if i == j or j == k or i == k:
            continue
        dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])

    # Frozen set so we can cache, also by doing f-{v} we're removing that valve so we can't turn it again
    @cache
    def search(t: int, u='AA', vs=frozenset(valve_flow), e=False):
        return max([valve_flow[v] * (t-dists[u, v]-1) + search(t-dists[u, v]-1, v, vs-{v}, e)
                    for v in vs if dists[u, v] < t] + [search(26, vs=vs) if e else 0])

    return search(26, e=True)


if __name__ == "__main__":
    print(part2(data))  # 2382
