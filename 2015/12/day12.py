import json
from pathlib import Path
from typing import cast

Document = int | str | list["Document"] | dict[str, "Document"]


def load_input() -> Document:
    with Path(__file__).parent.joinpath("input.txt").open() as f:
        return cast(Document, json.load(f))


def sum_numbers(doc: Document, *, ignore_red: bool = False) -> int:
    if isinstance(doc, int):
        return doc
    if isinstance(doc, list):
        return sum(sum_numbers(o, ignore_red=ignore_red) for o in doc)
    if isinstance(doc, dict) and (not ignore_red or "red" not in doc.values()):
        return sum(sum_numbers(v, ignore_red=ignore_red) for v in doc.values())
    return 0


def part_1(doc: Document) -> int:
    return sum_numbers(doc)


def part_2(doc: Document) -> int:
    return sum_numbers(doc, ignore_red=True)


if __name__ == "__main__":
    doc = load_input()
    print("Part 1:", part_1(doc))
    print("Part 2:", part_2(doc))
