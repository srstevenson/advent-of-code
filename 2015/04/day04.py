import hashlib
import itertools
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text()


def mine(key: str, prefix: str) -> int:
    for i in itertools.count(start=1):
        if hashlib.md5(f"{key}{i}".encode()).hexdigest().startswith(prefix):
            return i
    raise RuntimeError("Solution not found")


def part_1(key: str) -> int:
    return mine(key, "00000")


def part_2(key: str) -> int:
    return mine(key, "000000")


if __name__ == "__main__":
    key = load_input()
    print("Part 1:", part_1(key))
    print("Part 2:", part_2(key))
