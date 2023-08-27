import functools
import itertools
import math
from pathlib import Path


def load_input() -> int:
    return int(Path(__file__).parent.joinpath("input.txt").read_text())


@functools.cache
def factors(n: int) -> list[int]:
    factors = []
    for i in range(1, math.isqrt(n)):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)
    return factors


def part_1(min_presents: int) -> int:
    for house in itertools.count(start=1):
        if 10 * sum(factors(house)) >= min_presents:
            return house
    raise RuntimeError("Solution not found")


def part_2(min_presents: int) -> int:
    for house in itertools.count(start=1):
        if 11 * sum(f for f in factors(house) if house <= 50 * f) >= min_presents:
            return house
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    min_presents = load_input()
    print("Part 1:", part_1(min_presents))
    print("Part 2:", part_2(min_presents))
