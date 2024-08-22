import re
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def rotate_password(password: str) -> str:
    chars = list(password)
    for i in reversed(range(len(chars))):
        if chars[i] != "z":
            chars[i] = chr(ord(chars[i]) + 1)
            break
        chars[i] = "a"
    return "".join(chars)


def contains_increasing_triple(password: str) -> bool:
    return any(
        ord(password[i + 1]) == ord(password[i]) + 1
        and ord(password[i + 2]) == ord(password[i]) + 2
        for i in range(len(password) - 2)
    )


def contains_iol(password: str) -> bool:
    return bool(re.search("i|o|l", password))


def contains_two_pairs(password: str) -> bool:
    return len(re.findall(r"(\w)\1", password)) > 1


def is_valid(password: str) -> bool:
    return (
        contains_increasing_triple(password)
        and not contains_iol(password)
        and contains_two_pairs(password)
    )


def part_1(password: str) -> str:
    while not is_valid(password := rotate_password(password)):
        continue
    return password


if __name__ == "__main__":
    password = load_input()
    print("Part 1:", password := part_1(password))
    print("Part 2:", part_1(password))
