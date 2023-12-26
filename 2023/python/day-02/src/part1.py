import re
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


def part1(games_data: str) -> int:
    games_dict = data_to_dict(games_data)
    sum_ids = 0
    for (game_id, data) in games_dict.items():
        if data["red"] > 12 or data["green"] > 13 or data["blue"] > 14:
            continue
        sum_ids += game_id

    return sum_ids


def part1_v2(games_data: str) -> int:
    sum_possible_ids = 0
    for game in games_data:
        id = int(re.search(r'Game (\d+)', game).group(1))
        maxReds = max(map(int, re.findall(r'(\d+) red', game)))
        maxBlues = max(map(int, re.findall(r'(\d+) blue', game)))
        maxGreens = max(map(int, re.findall(r'(\d+) green', game)))
        if maxReds > 12 or maxBlues > 14 or maxGreens > 13:
            continue
        sum_possible_ids += id

    return sum_possible_ids


if __name__ == "__main__":
    print(part1(file_contents))
    print(part1_v2(file_contents))
