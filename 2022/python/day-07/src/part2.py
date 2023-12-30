from dotenv import load_dotenv
from collections import defaultdict
from itertools import accumulate
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


def part2(data: list[str]) -> int:
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

    folder_sizes = []

    def recalculate_size(folder: Folder):
        for child in folder.children.values():
            recalculate_size(child)
            folder.size += child.size
            folder_sizes.append(child.size)

    recalculate_size(root_folder)
    return min(size for size in folder_sizes if size >= root_folder.size-40_000_000)


def part2_v2(data: list[str]) -> int:
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
                # Add the size of the file to all the directories in the path
                for p in accumulate(curr):
                    dirs[p] += int(size)
    return min(size for size in dirs.values() if size >= dirs['/']-40_000_000)


if __name__ == "__main__":
    print(part2(data))  # 9847279
    print(part2_v2(data))
