import itertools
from pathlib import Path


def load_input() -> list[list[int]]:
    return [
        [int(side) for side in line.split()]
        for line in Path(__file__)
        .parent.joinpath("input.txt")
        .read_text()
        .strip()
        .splitlines()
    ]


def part_1(lines: list[list[int]]) -> int:
    return sum(a + b > c for a, b, c in (sorted(line) for line in lines))


def part_2(lines: list[list[int]]) -> int:
    return sum(
        a + b > c
        for batch in itertools.batched(lines, n=3)
        for i in range(3)
        for a, b, c in [sorted([batch[0][i], batch[1][i], batch[2][i]])]
    )


if __name__ == "__main__":
    lines = load_input()
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))
