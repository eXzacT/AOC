from dotenv import load_dotenv
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-19.txt'
with open(filename, 'r') as file:
    data = file.read()


def process_item(item: list[int], workflows_dict: dict[str, list[list[str], list[str], str]], start='in') -> int:
    while start:
        instructions = workflows_dict[start][0]
        validated = workflows_dict[start][1]
        try:
            next_instruction_address = workflows_dict[start][2]
        except:
            next_instruction_address = None

        for instruction_and_response in zip(instructions, validated):
            # Swap whatever we matched(x or m or a or s) with its value from the item
            instruction = re.sub(r"x|m|a|s", lambda match: item[(
                "xmas".index(match[0]))], instruction_and_response[0])

            if eval(instruction):
                # Passed instruction, check what to do next
                match(instruction_and_response[1]):
                    case 'A': return sum(int(val) for val in item)
                    case 'R': return 0
                    case _:
                        start = instruction_and_response[1]
                        break

        # Didn't pass any instruction, check if there is an extra address
        else:
            if next_instruction_address:
                if next_instruction_address == 'A':
                    return sum(int(val) for val in item)
                if next_instruction_address == 'R':
                    return 0
                # Neither accepted nor rejected, go to next address
                start = next_instruction_address
            else:  # No address, mark as accepted
                return sum(int(val) for val in item)


def part1(data: str) -> int:
    workflows_dict: dict[str, list[list[str], list[str], str]] = {}
    item_list: list[list[int]] = []

    workflows, items = data.split('\n\n')
    item_list.extend([num for num in re.findall(r'(\d+)', item)]
                     for item in items.split('\n'))

    for workflow in workflows.split('\n'):
        name, instructions = workflow[:-1].split('{')
        instructions_and_responses = instructions.split(',')
        next_address = instructions_and_responses.pop()
        workflows_dict[name] = list(
            map(list, zip(*[i_and_r.split(':') for i_and_r in instructions_and_responses])))
        workflows_dict[name].extend([next_address])

    return sum(process_item(item, workflows_dict) for item in item_list)


if __name__ == "__main__":
    print(part1(data))  # 330820

    '''
    Credit 4HbQ on reddit
    This solution blew my mind
    '''
    flows, parts = data.split('\n\n')

    def A_(): return 1 + x+m+a+s
    def R_(): return 1
    S_ = 0

    exec(flows.replace(':', ' and ').
         replace(',', '_() or ').
         replace('{', '_ = lambda: ').
         replace('}', '_()'))

    exec(parts.replace(',', ';').
         replace('{', '').
         replace('}', ';S_+=in_()-1'))

    print(S_)
