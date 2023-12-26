from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-13.txt'
with open(filename, 'r') as file:
    file_contents = [line.strip() for line in file]


def can_clear_smudge(s1: str, s2: str) -> bool:
    # Proceed only if the difference between '#' counts is 1
    diff = s1.count('#') - s2.count('#')
    if abs(diff) != 1:
        return False

    # Create a set of hash positions for each string
    pos1 = {i for i, c in enumerate(s1) if c == '#'}
    pos2 = {i for i, c in enumerate(s2) if c == '#'}

    # Check if there's exactly one difference in hash positions
    return len(pos1 ^ pos2) == 1


def process_pattern(pattern: list[str]) -> int:
    def check_mirror(start: int, end: int, cleared: bool) -> int:
        """
        Check if all the rows/cols are identical between start and end
        Returns the index of mirror ONLY if the smudge was cleared
        Otherwise 0 which means the rows/cols are not identical
        """
        while start < end:
            # Not equal and cannot be equal, make sure to change cleared bool
            if pattern[start] != pattern[end] and not (cleared := can_clear_smudge(pattern[start], pattern[end])):
                return 0
            start, end = start+1, end-1
        else:  # While loop ended successfully, return mirror index if cleared smudge
            if cleared:
                return start

    cleared = False
    # Compare all the other rows to the first one with a step of 2
    for idx in range(len(pattern) - 2, 0, -2):
        if pattern[0] == pattern[idx] or (cleared := can_clear_smudge(pattern[0], pattern[idx])):
            # Check whether all the patterns between these are also mirrored
            if (res := check_mirror(1, idx - 1, cleared)):
                return res
            else:  # Next loop is allowed to clear smudge again
                cleared = False

    cleared = False
    # Compare all the other rows to the last one with a step of 2
    for idx in range(1, len(pattern) - 1, 2):
        if pattern[-1] == pattern[idx] or (cleared := can_clear_smudge(pattern[-1], pattern[idx])):
            # Check whether all the patterns between these are also mirrored
            if (res := check_mirror(idx + 1, len(pattern) - 2, cleared)):
                return res
            else:  # Next loop is allowed to clear smudge again
                cleared = False
    return 0


def part2(input_list: list[str]) -> int:
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
    print(part2(file_contents))  # 44615
