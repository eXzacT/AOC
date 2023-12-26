from dotenv import load_dotenv
from collections import defaultdict
import numpy as np
import os

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-25.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file]


def part1(data: list[str]) -> int:
    graph = defaultdict(list)
    for line in data:
        left, right = line.split(': ')
        connects_to = right.split(' ')
        graph[left].extend(connects_to)
        for conn in connects_to:
            graph[conn].append(left)

    nodes = list(graph.keys())

    # Create a Laplacian matrix
    L = np.zeros((len(nodes), len(nodes)), int)
    for i, node in enumerate(nodes):
        degree = 0
        for _, connected_node in enumerate(graph[node]):
            L[i, nodes.index(connected_node)] = -1
            degree += 1

        L[i, i] = degree  # Diagonals count how many connections this vert has

    # Compute all eigenvalues and eigenvectors, then get the second smallest idx
    eigenvalues, eigenvectors = np.linalg.eig(L)
    idx = np.argsort(eigenvalues)[1]
    # Corresponding vector of the second smallest eigenvalue is the fiedler vector
    fiedler_vector = eigenvectors[:, idx]

    group1 = [val for val in fiedler_vector if val < 0]
    group2 = [val for val in fiedler_vector if val > 0]

    return len(group1)*len(group2)


if __name__ == "__main__":
    print(part1(data))
