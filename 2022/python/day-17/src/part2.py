from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-17.txt'
with open(filename, 'r') as file:
    data = file.read().strip()

CHAMBER_LEFT_WALL = 0
CHAMBER_RIGHT_WALL = 8
BLOCKS = 1_000_000_000_000


def part2(data: str) -> int:
    # Y position will change later by doing max_y+IMAG part
    blocks = [(3+4j, 4+4j, 5+4j, 6+4j),  # - shape
              (3+5j, 4+5j, 5+5j, 4+4j, 4+6j),  # + shape
              (3+4j, 4+4j, 5+4j, 5+5j, 5+6j),  # Reversed L shape
              (3+4j, 3+5j, 3+6j, 3+7j),  # | shape
              (3+4j, 4+4j, 3+5j, 4+5j)]  # square shape

    # Set ground as placed, usually I use x(REAL part) for row and y(IMAG part) for column,
    # but in this problem it made more sense to use cartesian coordinate system
    jets_len = len(data)
    blocks_len = len(blocks)
    placed = set([1+0j, 2+0j, 3+0j, 4+0j, 5+0j, 6+0j, 7+0j])
    cache = {}
    step = block_idx = jet_idx = max_y = 0

    # Spawn the first block
    block_parts_positions = blocks[block_idx]
    while step < BLOCKS:
        match data[jet_idx]:
            case '<':
                new_pos = [pos-1 for pos in block_parts_positions]
                # Is any position blocked by either another block or a wall?
                if not any(pos in placed or pos.real == CHAMBER_LEFT_WALL for pos in new_pos):
                    block_parts_positions = new_pos
            case '>':
                new_pos = [pos+1 for pos in block_parts_positions]
                # Is any position blocked by either another block or a wall?
                if not any(pos in placed or pos.real == CHAMBER_RIGHT_WALL for pos in new_pos):
                    block_parts_positions = new_pos

        jet_idx = (jet_idx+1) % jets_len

        # Can we move the block down?
        new_pos = [pos-1j for pos in block_parts_positions]
        if not any(pos in placed for pos in new_pos):
            block_parts_positions = new_pos
        else:
            # Place this block down, update highest position
            placed.update({pos for pos in block_parts_positions})
            max_rock_height = max(pos.imag for pos in block_parts_positions)
            max_y = max(max_y, max_rock_height)

            step += 1
            block_idx = step % blocks_len

            # Did we find a cycle?
            key = block_idx, jet_idx
            if key in cache:
                s, y = cache[key]
                diff = max_y-y
                cycle_len = step-s
                cycles = (BLOCKS-step)//(cycle_len)
                # Have to add max_y because that's what we got up until first cycle
                return diff*cycles+max_y
            else:
                # Store the current results and spawn another block
                cache[key] = step, max_y
                block_parts_positions = blocks[block_idx]
                block_parts_positions = [complex(pos.real, pos.imag+max_y)
                                         for pos in block_parts_positions]


if __name__ == "__main__":
    print(part2(data))  # 1560932944615
