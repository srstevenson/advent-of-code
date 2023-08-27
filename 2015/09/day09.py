import re
from collections import defaultdict
from collections.abc import Callable, Iterable
from itertools import pairwise, permutations
from pathlib import Path

Distances = dict[str, dict[str, int]]


def load_input() -> Distances:
    pattern = re.compile(r"(\w+) to (\w+) = (\d+)")
    distances: Distances = defaultdict(dict)
    lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
    for line in lines:
        if m := pattern.fullmatch(line):
            for i, j in [(1, 2), (2, 1)]:
                distances[m.group(i)][m.group(j)] = int(m.group(3))
    return distances


def extreme_distance(
    distances: Distances, *, reduce_fn: Callable[[Iterable[int]], int] = min
) -> int:
    return reduce_fn(
        sum(distances[a][b] for a, b in pairwise(path))
        for path in permutations(distances)
    )


def part_1(distances: Distances) -> int:
    return extreme_distance(distances)


def part_2(distances: Distances) -> int:
    return extreme_distance(distances, reduce_fn=max)


if __name__ == "__main__":
    distances = load_input()
    print("Part 1:", part_1(distances))
    print("Part 2:", part_2(distances))
