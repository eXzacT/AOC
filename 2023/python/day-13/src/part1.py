from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-13.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def process_pattern(pattern: list[str]) -> int:
    def check_mirror(start: int, end: int) -> int:
        """
        Check if all the rows/cols are identical between start and end
        Returns the index of mirror if there was one
        Otherwise 0 which means the rows/cols are not identical
        """
        while start < end:
            if pattern[start] != pattern[end]:
                return 0
            start, end = start+1, end-1
        else:  # While loop ended successfully, start represents mirror row/col idx
            return start

    # Compare all the other rows to the first one with a step of 2
    for idx in range(len(pattern) - 2, 0, -2):
        if pattern[0] == pattern[idx]:
            # Check whether all the patterns between these are also mirrored
            if (mirror_idx := check_mirror(1, idx - 1)):
                return mirror_idx

    # Compare all the other rows to the last one with a step of 2
    for idx in range(1, len(pattern) - 1, 2):
        if pattern[-1] == pattern[idx]:
            # Check whether all the patterns between these are also mirrored
            if (mirror_idx := check_mirror(idx + 1, len(pattern) - 2)):
                return mirror_idx
    return 0


def part1(input_list: list[str]) -> int:
    result = 0
    pattern = []

    for line in input_list+[""]:  # Add an empty line to process last batch
        if line:
            pattern.append(line)
        # Encountered an empty line, time to process the block we got so far
        else:
            # First try horizontally, if no mirrors were found 0 will be returned
            # So we can say OR because first part will return 100*0
            res = 100 * process_pattern(pattern) or process_pattern(
                [''.join(col) for col in zip(*pattern)])

            pattern.clear()
            result += res

    return result


if __name__ == "__main__":
    print(part1(file_contents))  # 30705
