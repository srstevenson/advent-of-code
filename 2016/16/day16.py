from itertools import batched
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def generate_checksum(data: str) -> str:
    return "".join("1" if x == y else "0" for x, y in batched(data, 2))


def correct_checksum(data: str, length: int) -> str:
    while len(data) < length:
        data = data + "0" + data[::-1].translate(str.maketrans("10", "01"))

    checksum = generate_checksum(data[:length])
    while len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)

    return checksum


def part_1(data: str) -> str:
    return correct_checksum(data, 272)


def part_2(data: str) -> str:
    return correct_checksum(data, 35651584)


if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
