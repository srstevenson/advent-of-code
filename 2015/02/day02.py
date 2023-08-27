from collections.abc import Iterable
from pathlib import Path
from typing import NamedTuple


class Box(NamedTuple):
    length: int
    width: int
    height: int


def load_input() -> list[Box]:
    return [
        Box(*map(int, line.split("x")))
        for line in Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
    ]


def wrapping_paper_area(box: Box) -> int:
    areas = [box.length * box.width, box.length * box.height, box.width * box.height]
    return 2 * sum(areas) + min(areas)


def ribbon_length(box: Box) -> int:
    perimeter = 2 * min(
        box.length + box.width, box.length + box.height, box.width + box.height
    )
    volume = box.length * box.width * box.height
    return perimeter + volume


def part_1(boxes: Iterable[Box]) -> int:
    return sum(map(wrapping_paper_area, boxes))


def part_2(boxes: Iterable[Box]) -> int:
    return sum(map(ribbon_length, boxes))


if __name__ == "__main__":
    boxes = load_input()
    print("Part 1:", part_1(boxes))
    print("Part 2:", part_2(boxes))
