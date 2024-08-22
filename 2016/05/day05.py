import hashlib
import itertools
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def part_1(door_id: str) -> str:
    password = []
    for index in itertools.count():
        digest = hashlib.md5(f"{door_id}{index}".encode()).hexdigest()
        if digest.startswith("00000"):
            password.append(digest[5])
            if len(password) == 8:
                return "".join(password)
    raise RuntimeError("Solution not found")


def part_2(door_id: str) -> str:
    password = [""] * 8
    for index in itertools.count():
        digest = hashlib.md5(f"{door_id}{index}".encode()).hexdigest()
        if (
            digest.startswith("00000")
            and digest[5].isdigit()
            and (position := int(digest[5])) < 8
            and password[position] == ""
        ):
            password[position] = digest[6]
            if all(password):
                return "".join(password)
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    door_id = load_input()
    print("Part 1:", part_1(door_id))
    print("Part 2:", part_2(door_id))
