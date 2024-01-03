from dotenv import load_dotenv
from collections import deque
import networkx as nx
import numpy as np
import numpy.typing as npt
import string
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-12.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): c for i, line in enumerate(file)
            for j, c in enumerate(line.strip())}
    file.seek(0)
    heights = np.array([[*line.strip()] for line in file.readlines()])


def part1(data: dict[complex, str]) -> int:
    # Previously used string.ascii_lowercase.index(c) but that's O(n)
    height = {c: ord(c) for c in string.ascii_lowercase}
    height['S'], height['E'] = 97, 122
    end = next(k for k, v in data.items() if v == 'E')
    queue = deque([(end, 0)])
    seen = set([end])

    while queue:
        pos, dist = queue.popleft()
        if data[pos] == 'S':  # Reached the start
            return dist

        for new_pos in [pos+1, pos-1, pos-1j, pos+1j]:
            if new_pos in data and new_pos not in seen:
                # Can only go 1 level higher but any level lower
                if height[data[pos]]-height[data[new_pos]] <= 1:
                    queue.append((new_pos, dist+1))
                    seen.add(new_pos)


def part1_networkx(heights: npt.NDArray):
    start = tuple(*np.argwhere(heights == 'S'))
    heights[start] = 'a'
    end = tuple(*np.argwhere(heights == 'E'))
    heights[end] = 'z'

    G: nx.DiGraph = nx.grid_2d_graph(*heights.shape, create_using=nx.DiGraph)
    G.remove_edges_from(
        [(a, b) for a, b in G.edges if ord(heights[b]) - ord(heights[a]) > 1])

    return nx.shortest_path_length(G, source=start, target=end)


if __name__ == "__main__":
    print(part1(data))  # 534
    print(part1_networkx(heights))
