import re
from collections import Counter
from pathlib import Path
from string import ascii_lowercase as alphabet
from typing import NamedTuple


class Room(NamedTuple):
    name: str
    sector: int
    checksum: str


def load_input() -> list[Room]:
    rooms: list[Room] = []
    pattern = re.compile(r"(\S+)-(\d+)\[(\w+)\]")
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for line in lines:
        if match := pattern.fullmatch(line):
            name, sector, checksum = match.groups()
            rooms.append(Room(name, int(sector), checksum))
    return rooms


def part_1(rooms: list[Room]) -> int:
    sectors = 0
    for room in rooms:
        counts = Counter(room.name.replace("-", ""))
        checksum = "".join(
            dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:5])
        )
        if checksum == room.checksum:
            sectors += room.sector
    return sectors


def part_2(rooms: list[Room]) -> int:
    for room in rooms:
        name = [
            " "
            if char == "-"
            else alphabet[(alphabet.index(char) + room.sector) % len(alphabet)]
            for char in room.name
        ]
        if "".join(name) == "northpole object storage":
            return room.sector

    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    rooms = load_input()
    print("Part 1:", part_1(rooms))
    print("Part 2:", part_2(rooms))
