from itertools import accumulate
from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-07.txt'
with open(filename, 'r') as file:
    data = [line.strip() for line in file.readlines()]


class Folder:
    def __init__(self, name: str, parent: str = "", size: int = 0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}

    def __repr__(self):
        return f"Folder {self.name}"


def part1(data: list[str]) -> int:
    curr_folder = root_folder = Folder('/')
    for line in data:
        if line.startswith('$ cd'):
            folder_name = line.split(' ')[2]
            if folder_name == '/':  # Skip root folder
                continue
            if folder_name != '..':
                curr_folder = curr_folder.children[folder_name]
            else:
                curr_folder = curr_folder.parent
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            folder_name = line.split(' ')[1]
            curr_folder.children.update(
                {folder_name: Folder(folder_name, parent=curr_folder)})
        else:
            size = line.split(' ')[0]
            curr_folder.size += int(size)

    goal_sizes = []

    def recalculate_size(folder: Folder):
        for child in folder.children.values():
            recalculate_size(child)
            folder.size += child.size
        if folder.size <= 100_000:
            goal_sizes.append(folder.size)

    recalculate_size(root_folder)
    return sum(goal_sizes)


def part1_v2(data: list[str]) -> int:
    '''4HbQ on reddit, beautiful solution!'''
    dirs = defaultdict(int)

    for line in data:
        match line.split():
            case '$', 'cd', '/': curr = ['/']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)

    return sum(size for size in dirs.values() if size <= 100_000)


if __name__ == "__main__":
    print(part1(data))  # 1315285
    print(part1_v2(data))
