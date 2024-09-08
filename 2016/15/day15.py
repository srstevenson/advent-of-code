import re
from pathlib import Path
from typing import Final, NamedTuple

DISC_PATTERN: Final = re.compile(
    r"Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)."
)


class Disc(NamedTuple):
    num_positions: int
    start_position: int


def load_input() -> list[Disc]:
    return [
        Disc(*map(int, match.groups()))
        for line in Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
        if (match := DISC_PATTERN.fullmatch(line))
    ]


def find_first_time(discs: list[Disc]) -> int:
    time, step = 0, 1
    for index, disc in enumerate(discs, start=1):
        while (disc.start_position + index + time) % disc.num_positions != 0:
            time += step
        step *= disc.num_positions
    return time


def part_1(discs: list[Disc]) -> int:
    return find_first_time(discs)


def part_2(discs: list[Disc]) -> int:
    return find_first_time([*discs, Disc(11, 0)])


if __name__ == "__main__":
    discs = load_input()
    print("Part 1:", part_1(discs))
    print("Part 2:", part_2(discs))
