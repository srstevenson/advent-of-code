import re
from collections import defaultdict
from itertools import pairwise, permutations
from pathlib import Path

Happiness = dict[str, dict[str, int]]


def load_input() -> Happiness:
    happiness: Happiness = defaultdict(lambda: defaultdict(int))
    pattern = re.compile(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\."
    )
    lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
    for line in lines:
        if match := pattern.fullmatch(line):
            left, sign, amount, right = match.groups()
            happiness[left][right] = int(amount) if sign == "gain" else -int(amount)
    return happiness


def find_max_change(happiness: Happiness, *, add_you: bool = False) -> int:
    attendees = list(happiness)
    if add_you:
        attendees.append("You")
    return max(
        sum(
            happiness[left][right] + happiness[right][left]
            for left, right in pairwise([attendees[0], *perm, attendees[0]])
        )
        for perm in permutations(attendees[1:])
    )


def part_1(happiness: Happiness) -> int:
    return find_max_change(happiness)


def part_2(happiness: Happiness) -> int:
    return find_max_change(happiness, add_you=True)


if __name__ == "__main__":
    happiness = load_input()
    print("Part 1:", part_1(happiness))
    print("Part 2:", part_2(happiness))
