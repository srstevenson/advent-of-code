import re
from collections.abc import Iterable
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def part_1(strings: Iterable[str]) -> int:
    def contains_vowels(string: str) -> bool:
        return len(re.findall("[aeiou]", string)) >= 3

    def contains_pair(string: str) -> bool:
        return bool(re.search(r"(\w)\1", string))

    def no_forbidden(string: str) -> bool:
        return not re.search("ab|cd|pq|xy", string)

    def is_nice(string: str) -> bool:
        return (
            contains_vowels(string) and contains_pair(string) and no_forbidden(string)
        )

    return sum(map(is_nice, strings))


def part_2(strings: Iterable[str]) -> int:
    def contains_pair(string: str) -> bool:
        return bool(re.search(r"(\w{2}).*\1", string))

    def contains_repeat(string: str) -> bool:
        return bool(re.search(r"(\w).\1", string))

    def is_nice(string: str) -> bool:
        return contains_pair(string) and contains_repeat(string)

    return sum(map(is_nice, strings))


if __name__ == "__main__":
    strings = load_input()
    print("Part 1:", part_1(strings))
    print("Part 2:", part_2(strings))
