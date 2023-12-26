from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()

filename = os.getenv('TEXTS_PATH')+'day-02.txt'
with open(filename, 'r') as file:
    file_contents = file.readlines()


def data_to_dict(game_data: str) -> dict[dict]:
    games_dict = {}

    for line in game_data:
        line = line.strip()
        game, data = line.split(': ')
        game_id = int(game.split(' ')[1])
        games_dict[game_id] = defaultdict(int)
        for item in data.split('; '):
            for color_data in item.split(', '):
                count, color = color_data.split(' ')
                games_dict[game_id][color] = max(
                    games_dict[game_id][color], int(count))

    return games_dict


def part2(games_data: str) -> int:
    games_dict = data_to_dict(games_data)
    sum_power_sets = 0
    for data in games_dict.values():
        sum_power_sets += data["red"]*data["blue"]*data["green"]

    return sum_power_sets


if __name__ == "__main__":
    print(part2(file_contents))
