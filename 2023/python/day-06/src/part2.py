from dotenv import load_dotenv
import os
import re
import math

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-06.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def part2(input_list: list[str]) -> int:
    race_time = int(''.join(re.findall(r'\d+', input_list[0])))
    record_distance = int(''.join(re.findall(r'\d+', input_list[1])))
    count = 0
    for hold_time in range(1, race_time):
        remaining_time = race_time-hold_time
        if hold_time*remaining_time > record_distance:
            count += 1
    return count


def part2_binary_search(input_list: list[str]) -> int:
    race_time = int(''.join(re.findall(r'\d+', input_list[0])))
    record_distance = int(''.join(re.findall(r'\d+', input_list[1])))

    def did_win(hold_time: int):
        return hold_time * (race_time - hold_time) > record_distance

    def binary_search_then_walk(start: int, end: int, backwards=False):
        while start < end:
            mid = start + (end-start) // 2
            if (did_win(mid) if backwards else not did_win(mid)):
                end = mid
            else:
                start = mid + 1

        return start

    middle = race_time//2
    min_optimal_hold = binary_search_then_walk(1, middle, backwards=True)
    max_optimal_hold = binary_search_then_walk(middle, race_time)

    return max_optimal_hold-min_optimal_hold


def part2_quadratic_formula(input_list: list[str]) -> int:
    race_time = int(''.join(re.findall(r'\d+', input_list[0])))
    record_distance = int(''.join(re.findall(r'\d+', input_list[1])))

    # Quadratic equation(distance=(race_time*x)*x)
    # x represents holding time
    max_optimal_hold = (
        race_time + math.sqrt(race_time**2-4*1*record_distance))//2
    min_optimal_hold = (
        race_time - math.sqrt(race_time**2-4*1*record_distance))//2
    return max_optimal_hold-min_optimal_hold


if __name__ == "__main__":
    print(part2(file_contents))  # 36992486
    print(part2_binary_search(file_contents))
    print(part2_quadratic_formula(file_contents))
