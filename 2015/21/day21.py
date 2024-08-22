from copy import copy
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import NamedTuple


@dataclass
class Character:
    damage: int
    armor: int
    hit_points: int


@dataclass
class Player(Character):
    cost: int = 0


class Item(NamedTuple):
    cost: int
    damage: int
    armor: int


WEAPONS = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0),
]

ARMORS = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5),
]

RINGS = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3),
]


def load_input() -> Character:
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    return Character(
        **{
            (stat := line.partition(": "))[0].lower().replace(" ", "_"): int(stat[2])
            for line in lines
        }
    )


def generate_players(*, reverse: bool = False) -> list[Player]:
    p = Player(damage=0, armor=0, hit_points=100)

    no_rings = [
        Player(
            damage=p.damage + w.damage,
            armor=p.armor + w.armor,
            hit_points=p.hit_points,
            cost=p.cost + w.cost,
        )
        for w in WEAPONS
    ]

    one_armor = [
        Player(
            damage=p.damage + a.damage,
            armor=p.armor + a.armor,
            hit_points=p.hit_points,
            cost=p.cost + a.cost,
        )
        for p, a in product(no_rings, ARMORS)
    ]
    no_rings.extend(one_armor)

    one_ring = [
        Player(
            damage=p.damage + r.damage,
            armor=p.armor + r.armor,
            hit_points=p.hit_points,
            cost=p.cost + r.cost,
        )
        for p, r in product(no_rings, RINGS)
    ]

    two_rings = [
        Player(
            damage=p.damage + r1.damage + r2.damage,
            armor=p.armor + r1.armor + r2.armor,
            hit_points=p.hit_points,
            cost=p.cost + r1.cost + r2.cost,
        )
        for p, (r1, r2) in product(no_rings, combinations(RINGS, r=2))
    ]

    return sorted(
        no_rings + one_ring + two_rings, key=lambda p: p.cost, reverse=reverse
    )


def player_wins(player: Character, boss: Character) -> bool:
    attacker, defender = player, boss
    while True:
        defender.hit_points -= max(1, attacker.damage - defender.armor)
        if defender.hit_points <= 0:
            return defender is boss
        attacker, defender = defender, attacker


def part_1(boss: Character) -> int:
    for player in generate_players():
        if player_wins(player, copy(boss)):
            return player.cost
    raise RuntimeError("Solution not found")


def part_2(boss: Character) -> int:
    for player in generate_players(reverse=True):
        if not player_wins(player, copy(boss)):
            return player.cost
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    boss = load_input()
    print("Part 1:", part_1(boss))
    print("Part 2:", part_2(boss))
