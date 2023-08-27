import ast
import re
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def encode(string: str) -> str:
    return '"' + re.escape(string).replace('"', '\\"') + '"'


def part_1(strings: list[str]) -> int:
    return sum(len(s) - len(ast.literal_eval(s)) for s in strings)


def part_2(strings: list[str]) -> int:
    return sum(len(encode(s)) - len(s) for s in strings)


if __name__ == "__main__":
    strings = load_input()
    print("Part 1:", part_1(strings))
    print("Part 2:", part_2(strings))
