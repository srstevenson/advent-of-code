from collections import Counter
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()


def find_message(messages: list[str], index: int) -> str:
    return "".join(
        Counter(m[i] for m in messages).most_common()[index][0]
        for i in range(len(messages[0]))
    )


def part_1(messages: list[str]) -> str:
    return find_message(messages, 0)


def part_2(messages: list[str]) -> str:
    return find_message(messages, -1)


if __name__ == "__main__":
    messages = load_input()
    print("Part 1:", part_1(messages))
    print("Part 2:", part_2(messages))
