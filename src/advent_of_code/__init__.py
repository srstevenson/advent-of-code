from datetime import datetime
from itertools import product
from pathlib import Path
from typing import NamedTuple

import aocd  # type: ignore[reportMissingImports]

SOLUTION_TEMPLATE = """
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def part_1(input_data: str) -> None:
    return None


def part_2(input_data: str) -> None:
    return None


if __name__ == "__main__":
    input_data = load_input()
    print("Part 1:", part_1(input_data))
    print("Part 2:", part_2(input_data))
""".lstrip()


class Day(NamedTuple):
    year: int
    day: int
    directory: Path


def directory_for_day(year: int, day: int) -> Path:
    return Path(f"{year}/{day:0>2}")


def next_uninitialised_day() -> Day | None:
    for year, day in product(range(2015, datetime.today().year + 1), range(1, 26)):
        directory = directory_for_day(year, day)
        if not directory.exists():
            return Day(year, day, directory)
    return None


def initialise_day(day: Day) -> None:
    input_data = aocd.get_data(year=day.year, day=day.day)
    day.directory.mkdir(parents=True)
    day.directory.joinpath("input.txt").write_text(input_data)
    day.directory.joinpath(f"day{day.day:0>2}.py").write_text(SOLUTION_TEMPLATE)


def initialise_next_day() -> None:
    if day := next_uninitialised_day():
        initialise_day(day)
        print(f"Initialised {day.year} day {day.day} in {day.directory}")
    else:
        print("All days are complete")
