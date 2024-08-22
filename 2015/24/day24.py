import itertools
import math
from collections.abc import Sequence
from pathlib import Path


def load_input() -> list[int]:
    return list(
        map(
            int,
            Path(__file__)
            .parent.joinpath("input.txt")
            .read_text()
            .strip()
            .splitlines(),
        )
    )


def find_min_qe(packages: Sequence[int], groups: int) -> int:
    weight = sum(packages) // groups
    for r in range(1, len(packages)):
        qes = [
            math.prod(group)
            for group in itertools.combinations(packages, r=r)
            if sum(group) == weight
        ]
        if qes:
            return min(qes)
    raise RuntimeError("Solution not found")


def part_1(packages: Sequence[int]) -> int:
    return find_min_qe(packages, 3)


def part_2(packages: Sequence[int]) -> int:
    return find_min_qe(packages, 4)


if __name__ == "__main__":
    packages = load_input()
    print("Part 1:", part_1(packages))
    print("Part 2:", part_2(packages))
