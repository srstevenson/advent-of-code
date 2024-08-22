import math
import re
from collections import Counter
from collections.abc import Mapping
from itertools import combinations_with_replacement
from pathlib import Path
from typing import NamedTuple


class Properties(NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def load_input() -> dict[str, Properties]:
    pattern = re.compile(
        r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), "
        r"texture (-?\d+), calories (-?\d+)"
    )
    properties = {}
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for line in lines:
        if match := pattern.fullmatch(line):
            ingredient, *props = match.groups()
            properties[ingredient] = Properties(*map(int, props))
    return properties


def find_best_score(
    properties: Mapping[str, Properties], *, constrain_calories: bool = False
) -> int:
    max_score = 0
    for combination in combinations_with_replacement(properties, 100):
        scores = {
            "capacity": 0,
            "durability": 0,
            "flavor": 0,
            "texture": 0,
            "calories": 0,
        }
        for ingredient, count in Counter(combination).items():
            for score in scores:
                scores[score] += getattr(properties[ingredient], score) * count
        if constrain_calories and scores["calories"] != 500:
            continue
        max_score = max(
            max_score,
            math.prod(max(0, scores[prop]) for prop in scores if prop != "calories"),
        )
    return max_score


def part_1(properties: Mapping[str, Properties]) -> int:
    return find_best_score(properties)


def part_2(properties: Mapping[str, Properties]) -> int:
    return find_best_score(properties, constrain_calories=True)


if __name__ == "__main__":
    properties = load_input()
    print("Part 1:", part_1(properties))
    print("Part 2:", part_2(properties))
