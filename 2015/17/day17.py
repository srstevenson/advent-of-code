from collections import defaultdict
from collections.abc import Sequence
from itertools import combinations
from pathlib import Path


def load_input() -> list[int]:
    return list(
        map(int, Path(__file__).parent.joinpath("input.txt").read_text().splitlines())
    )


def part_1(capacities: Sequence[int]) -> int:
    ways = defaultdict(int)
    ways[0] = 1
    for capacity in capacities:
        for total in reversed(range(151)):
            ways[total] += ways[total - capacity]
    return ways[150]


def part_2(capacities: Sequence[int]) -> int:
    for r in range(1, len(capacities)):
        ways = sum(sum(c) == 150 for c in combinations(capacities, r=r))
        if ways > 0:
            return ways
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    capacities = load_input()
    print("Part 1:", part_1(capacities))
    print("Part 2:", part_2(capacities))
