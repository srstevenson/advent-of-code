import functools
import hashlib
import itertools
import re
from pathlib import Path
from typing import Final

THREE_CHARS: Final = re.compile(r"(.)\1\1")


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


@functools.cache
def generate_hash(string: str, *, stretch: bool = False) -> str:
    digest = hashlib.md5(string.encode()).hexdigest()
    if stretch:
        for _ in range(2016):
            digest = hashlib.md5(digest.encode()).hexdigest()
    return digest


def index_for_key_64(salt: str, *, stretch: bool = False) -> int:
    keys_found = 0
    for index in itertools.count():
        digest = generate_hash(f"{salt}{index}", stretch=stretch)
        if match := THREE_CHARS.search(digest):
            char = match.group(0)[0]
            if any(
                char * 5 in generate_hash(f"{salt}{index + delta}", stretch=stretch)
                for delta in range(1, 1001)
            ):
                keys_found += 1
                if keys_found == 64:
                    return index

    raise RuntimeError("Solution not found")


def part_1(salt: str) -> int:
    return index_for_key_64(salt)


def part_2(salt: str) -> int:
    return index_for_key_64(salt, stretch=True)


if __name__ == "__main__":
    salt = load_input()
    print("Part 1:", part_1(salt))
    print("Part 2:", part_2(salt))
