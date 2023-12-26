from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-19.txt'
with open(filename, 'r') as file:
    data = file.read()


def check_overlap(x1: int, y1: int, x2: int, y2: int):
    # Check for no overlap
    if y1 <= x2 or y2 <= x1:
        return ((x1, y1), (0, 0), False)

    # Find the overlapping range
    overlap_start = max(x1, x2)
    overlap_end = min(y1, y2)

    # Find the remaining range to use in next loop
    if overlap_start > x1:
        remaining = (x1, overlap_start)
    elif overlap_end < y1:
        remaining = (overlap_end, y1)

    return ((overlap_start, overlap_end), remaining, True)


def distinct_accepted_combinations(workflows_dict: dict[str, list[list[str], list[str], str]]) -> int:
    # Stores all the accepted combinations of xmas ranges
    accepted: list[tuple[int, int]] = []

    def helper(x=(1, 4001), m=(1, 4001), a=(1, 4001), s=(1, 4001), start="in") -> None:
        # Reject and accept base cases
        if start == 'R':
            return
        if start == 'A':
            accepted.append([x, m, a, s])
            return

        instructions = workflows_dict[start][0]
        responses = workflows_dict[start][1]
        try:
            next_instruction_address = workflows_dict[start][2]
        except:
            next_instruction_address = None

        for i_and_r in zip(instructions, responses):
            instruction = i_and_r[0]
            location_id = i_and_r[1]

            c, c_range = instruction[0], instruction[1:]
            lower_r, upper_r = c_range.split('-')
            lower_r = int(lower_r)
            upper_r = int(upper_r)

            # Update range for matching character
            match c:
                case 'x':
                    new_range, remainder, overlapped = check_overlap(
                        x[0], x[1], lower_r,  upper_r)
                    if not overlapped:
                        continue
                    # Recursively call for the new location and new range
                    helper(new_range, m, a, s, location_id)
                    # Update range that we will use next loop(simulate failing the predicate)
                    x = remainder
                case 'm':
                    new_range, remainder, overlapped = check_overlap(
                        m[0], m[1], lower_r,  upper_r)
                    if not overlapped:
                        continue
                    helper(x, new_range, a, s, location_id)
                    m = remainder
                case 'a':
                    new_range, remainder, overlapped = check_overlap(
                        a[0], a[1], lower_r,  upper_r)
                    if not overlapped:
                        continue
                    helper(x, m, new_range, s, location_id)
                    a = remainder
                case 's':
                    new_range, remainder, overlapped = check_overlap(
                        s[0], s[1], lower_r,  upper_r)
                    if not overlapped:
                        continue
                    helper(x, m, a, new_range, location_id)
                    s = remainder

        # Didn't pass any instructions but next address exists
        if next_instruction_address:
            return helper(x, m, a, s, next_instruction_address)

        # No matches, accept by default
        # Apparently it never gets here
        # accepted.append([x, m, a, s])

    helper()
    return sum([(x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0]) for x, m, a, s in accepted])


def part2(data: str) -> int:
    workflows_dict: dict[str, list[list[str], list[str], str]] = {}
    workflows, _ = data.split('\n\n')

    # Replace comparison operators with ranges
    workflows = workflows.replace('<', '1-')
    workflows = re.sub(
        r'>(\d+)', lambda match: str(int(match[1])+1)+"-4001", workflows)

    for workflow in workflows.split('\n'):
        name, instructions = workflow[:-1].split('{')
        instructions_and_responses = instructions.split(',')
        next_address = instructions_and_responses.pop()
        workflows_dict[name] = list(
            map(list, zip(*[i_and_r.split(':') for i_and_r in instructions_and_responses])))
        workflows_dict[name].extend([next_address])

    return distinct_accepted_combinations(workflows_dict)


if __name__ == "__main__":
    print(part2(data))  # 123972546935551
