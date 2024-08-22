import collections
import enum
import functools
import sys
from pathlib import Path
from typing import NamedTuple, cast


def load_input() -> tuple[int, int]:
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    return cast(tuple[int, int], tuple(int(line.split(": ")[1]) for line in lines))


class Spell(enum.Enum):
    MAGIC_MISSILE = 53
    DRAIN = 73
    SHIELD = 113
    POISON = 173
    RECHARGE = 229


class GameState(NamedTuple):
    boss_hp: int
    boss_damage: int
    wizard_hp: int
    wizard_armor: int
    mana: int
    shield_turns: int
    poison_turns: int
    recharge_turns: int
    mana_spent: int


def apply_effects(gs: GameState) -> GameState:
    boss_hp = gs.boss_hp - 3 if gs.poison_turns else gs.boss_hp
    mana = gs.mana + 101 if gs.recharge_turns else gs.mana
    return gs._replace(
        boss_hp=boss_hp,
        wizard_armor=7 if gs.shield_turns else 0,
        mana=mana,
        shield_turns=max(0, gs.shield_turns - 1),
        poison_turns=max(0, gs.poison_turns - 1),
        recharge_turns=max(0, gs.recharge_turns - 1),
    )


def take_wizard_turn(gs: GameState, spell: Spell) -> GameState:
    match spell:
        case Spell.MAGIC_MISSILE:
            boss_hp = gs.boss_hp - 4
        case Spell.DRAIN:
            boss_hp = gs.boss_hp - 2
        case _:
            boss_hp = gs.boss_hp

    wizard_hp = gs.wizard_hp + 2 if spell == Spell.DRAIN else gs.wizard_hp

    return gs._replace(
        boss_hp=boss_hp,
        wizard_hp=wizard_hp,
        mana=gs.mana - spell.value,
        shield_turns=6 if spell == Spell.SHIELD else gs.shield_turns,
        poison_turns=6 if spell == Spell.POISON else gs.poison_turns,
        recharge_turns=5 if spell == Spell.RECHARGE else gs.recharge_turns,
        mana_spent=gs.mana_spent + spell.value,
    )


def take_boss_turn(gs: GameState) -> GameState:
    return gs._replace(
        wizard_hp=gs.wizard_hp - max(1, gs.boss_damage - gs.wizard_armor)
    )


@functools.cache
def play_round(  # noqa: PLR0911
    gs: GameState, spell: Spell, *, hard: bool
) -> GameState | int | None:
    if hard:
        gs = gs._replace(wizard_hp=gs.wizard_hp - 1)
        if gs.wizard_hp <= 0:
            return None

    gs = apply_effects(gs)

    if gs.boss_hp <= 0:
        return gs.mana_spent

    if spell.value > gs.mana or (
        (spell == Spell.SHIELD and gs.shield_turns)
        or (spell == Spell.POISON and gs.poison_turns)
        or (spell == Spell.RECHARGE and gs.recharge_turns)
    ):
        return None

    gs = take_wizard_turn(gs, spell)
    if gs.boss_hp <= 0:
        return gs.mana_spent

    gs = apply_effects(gs)
    if gs.boss_hp <= 0:
        return gs.mana_spent

    gs = take_boss_turn(gs)
    if gs.wizard_hp <= 0:
        return None

    return gs


def find_min_winning_spend(boss_stats: tuple[int, int], *, hard: bool = False) -> int:
    gs = GameState(
        boss_hp=boss_stats[0],
        boss_damage=boss_stats[1],
        wizard_hp=50,
        wizard_armor=0,
        mana=500,
        shield_turns=0,
        poison_turns=0,
        recharge_turns=0,
        mana_spent=0,
    )

    queue = collections.deque([gs])
    min_spend = sys.maxsize

    while queue:
        gs = queue.pop()
        for spell in Spell:
            outcome = play_round(gs, spell, hard=hard)
            if isinstance(outcome, GameState) and gs.mana_spent < min_spend:
                queue.appendleft(outcome)
            elif isinstance(outcome, int) and outcome < min_spend:
                min_spend = outcome
    return min_spend


def part_1(boss_stats: tuple[int, int]) -> int:
    return find_min_winning_spend(boss_stats)


def part_2(boss_stats: tuple[int, int]) -> int:
    return find_min_winning_spend(boss_stats, hard=True)


if __name__ == "__main__":
    boss_stats = load_input()
    print("Part 1:", part_1(boss_stats))
    print("Part 2:", part_2(boss_stats))
