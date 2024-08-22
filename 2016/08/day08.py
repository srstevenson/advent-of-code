import re
from itertools import product
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()


def follow(instructions: list[str]) -> list[list[bool]]:
    screen = [[False] * 50 for _ in range(6)]
    for inst in instructions:
        if match := re.fullmatch(r"rect (\d+)x(\d+)", inst):
            cols, rows = map(int, match.groups())
            for row, col in product(range(rows), range(cols)):
                screen[row][col] = True
        elif match := re.fullmatch(r"rotate column x=(\d+) by (\d+)", inst):
            col, count = map(int, match.groups())
            orig = [screen[row][col] for row in range(len(screen))]
            for row in range(len(screen)):
                screen[row][col] = orig[row - count % len(orig)]
        elif match := re.fullmatch(r"rotate row y=(\d+) by (\d+)", inst):
            row, count = map(int, match.groups())
            orig = screen[row].copy()
            for col in range(len(screen[0])):
                screen[row][col] = orig[col - count % len(orig)]
    return screen


def part_1(screen: list[list[bool]]) -> int:
    return sum(sum(row) for row in screen)


def part_2(screen: list[list[bool]]) -> str:
    return "\n" + "\n".join(
        "".join("█" if pixel else " " for pixel in row) for row in screen
    )


if __name__ == "__main__":
    instructions = load_input()
    screen = follow(instructions)
    print("Part 1:", part_1(screen))
    print("Part 2:", part_2(screen))
