from dotenv import load_dotenv
import os
import re
from functools import reduce

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-15.txt'
with open(filename, 'r') as file:
    file_contents = file.read().strip()


def part2(input_str: str) -> int:
    boxes = {i: {} for i in range(256)}
    for data in input_str.split(','):

        operation = re.search(r'=|-', data).group()
        label, focal_power = data.split(operation)

        idx = reduce(lambda carry, c: (carry+ord(c))*17 % 256, label, 0)

        if operation == '-':  # Remove the lens if we could find it
            boxes[idx].pop(label, None)
        else:  # Replace the lens if there was one, otherwise just put the new one
            focal_power = int(focal_power)
            boxes[idx].update({label: focal_power})

    # Box index multiplied with the sum of focal powers multiplied with their pos
    return sum((box_idx+1) * sum(lens_idx * val for lens_idx, val in enumerate(lenses.values(), 1))
               for box_idx, lenses in boxes.items())


if __name__ == "__main__":
    print(part2(file_contents))  # 239484
