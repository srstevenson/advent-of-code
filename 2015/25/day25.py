import re
from pathlib import Path
from typing import cast


def load_input() -> tuple[int, int]:
    text = Path(__file__).parent.joinpath("input.txt").read_text().strip()
    if match := re.search(r"row (\d+), column (\d+).", text):
        return cast(tuple[int, int], tuple(map(int, match.groups())))
    raise RuntimeError("Invalid input file")


def part_1(target_row: int, target_col: int) -> int:
    row, col, code = 1, 1, 20151125
    while code := (code * 252533) % 33554393:
        if row == 1:
            row, col = col + 1, 1
        else:
            row -= 1
            col += 1
        if row == target_row and col == target_col:
            return code
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    coordinates = load_input()
    print("Part 1:", part_1(*coordinates))
