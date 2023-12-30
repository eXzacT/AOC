from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-08.txt'
with open(filename, 'r') as file:
    data = {complex(i, j): (int(c), False) for i, row in enumerate(file)
            for j, c in enumerate(row.strip())}

WIDTH, HEIGHT = (99, 99) if __name__ == "__main__" else (5, 5)


def part1(data: dict[complex, str]) -> int:
    visible_trees = 0
    for i in range(1, WIDTH-1):
        for j in range(1, HEIGHT-1):
            pos = complex(i, j)
            curr_tree_height = data[pos]
            # Go in every direction break early if reaching the edge is possible
            for d in [1, -1, -1j, 1j]:
                new_pos = pos+d
                # Keep going in the current direction until blocked by a taller tree
                while data[new_pos] < curr_tree_height:
                    new_pos += d
                    if new_pos not in data:  # Got to end without being blocked
                        visible_trees += 1
                        break
                else:  # Means the while loop finished without breaking, so check other directions
                    continue
                # This means we broke from the while loop, break again(neat trick to avoid flags but a bit confusing)
                break

    # Add edges aswell - corners
    return visible_trees+WIDTH*2+HEIGHT*2-4


if __name__ == "__main__":
    print(part1(data))  # 1809
