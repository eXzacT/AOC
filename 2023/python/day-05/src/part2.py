from dotenv import load_dotenv
import os
import re

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-05.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


# Works for test input but not for the actual file because the approach is slow
def part2(lines: list[str]) -> int:
    # First line contains the start locations(aka seeds)
    lines_iter = iter(lines)

    seed_ranges = [int(num)
                   for num in re.findall(r'\d+', next(lines_iter))]

    start_locations: tuple[int, bool] = []
    for idx in range(0, len(seed_ranges), 2):
        start = seed_ranges[idx]
        end = start + seed_ranges[idx+1]
        start_locations.extend([num, False] for num in range(start, end))

    for line in lines_iter:

        if ':' in line:
            # Reset bool flag so the numbers can be changed again later
            start_locations = [(location, False)
                               for location, _ in start_locations]

        # Process only lines that have numerical values
        found_nums = [int(num) for num in re.findall(r'\d+', line)]
        if found_nums:
            start = found_nums[1]
            end = start + found_nums[2]
            diff = start - found_nums[0]

            start_locations = [
                (location-diff, True)
                if not wasChanged and start <= location < end
                else (location, wasChanged)
                for location, wasChanged in start_locations
            ]

    return min(start_locations)[0]


def part2_v2(lines: list[str]) -> int:
    lines_iter = iter(lines)

    seed_ranges = [int(num)
                   for num in re.findall(r'\d+', next(lines_iter))]

    start_locations: list[tuple[int, int, bool]] = []
    for idx in range(0, len(seed_ranges), 2):
        start = seed_ranges[idx]
        end = start + seed_ranges[idx+1]
        start_locations.append((start, end, False))

    for line in lines_iter:
        if ':' in line:
            start_locations = [(start, end, False)
                               for start, end, _ in start_locations]

        found_nums = [int(num) for num in re.findall(r'\d+', line)]
        if found_nums:
            start = found_nums[1]
            end = start + found_nums[2]
            diff = start - found_nums[0]

            new_start_locations = []
            for loc_start, loc_end, was_changed in start_locations:
                # Doesn't matter if it overlaps, was changed so just keep it
                if was_changed:
                    new_start_locations.append(
                        (loc_start, loc_end, was_changed))
                    continue

                # Entire range overlaps
                if start <= loc_start and end >= loc_end:
                    new_start_locations.append(
                        (loc_start-diff, loc_end-diff, True))
                # Middle of the range overlaps
                elif loc_start <= end <= loc_end and loc_start <= start <= loc_end:
                    new_start_locations.append(
                        (loc_start, start, False))
                    new_start_locations.append(
                        (start-diff, end-diff, True))
                    new_start_locations.append(
                        (end, loc_end, False))
                # Left part overlaps
                elif loc_start <= end <= loc_end:
                    new_start_locations.append(
                        (loc_start-diff, end-diff, True))
                    new_start_locations.append(
                        (end, loc_end, False))
                # Right part overlaps
                elif loc_start <= start <= loc_end:
                    new_start_locations.append(
                        (start-diff, loc_end-diff, True))
                    new_start_locations.append(
                        (loc_start, start, False))
                # Nothing overlaps, keep intact
                else:
                    new_start_locations.append(
                        (loc_start, loc_end, was_changed))

            start_locations = new_start_locations

    return min(start for start, _, _ in start_locations)


if __name__ == "__main__":
    # print(part2(file_contents))
    print(part2_v2(file_contents))  # 52510809
