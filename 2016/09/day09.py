from functools import cache
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


@cache
def decompress(data: str, *, recurse: bool) -> int:
    i = length = 0
    while i < len(data):
        if data[i] == "(":
            i += 1
            marker = []
            while data[i] != ")":
                marker.append(data[i])
                i += 1
            i += 1
            chars, repeat = map(int, "".join(marker).split("x"))
            if recurse:
                length += decompress(data[i : i + chars], recurse=True) * repeat
            else:
                length += chars * repeat
            i += chars
        else:
            length += 1
            i += 1
    return length


def part_1(data: str) -> int:
    return decompress(data, recurse=False)


def part_2(data: str) -> int:
    return decompress(data, recurse=True)


if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
