import pytest
from tournament_game import (
    armor_crush_model,
    Character,
)


@pytest.mark.parametrize(
    "damage",
    [
        0,
        60,
        97,
        15.124,
        38.2,
        21.456,
        31,
        20,
        43,
        0.752,
    ],
)
def test_armor_crush_model_abs(damage):
    loser = Character("Loser")
    loser.armor_curr = 0
    armor_crush_model(loser, damage)
    result = loser.armor_curr
    assert result <= loser.armor


@pytest.mark.parametrize(
    "damage",
    [
        0,
        60,
        97,
        15.124,
        38.2,
        21.456,
        31,
        20,
        43,
        0.752,
    ],
)
def test_armor_crush_model_direct(damage):
    loser = Character("Loser")
    loser.armor_curr = 0
    expected_result = round((loser.armor_curr - damage), 1)
    armor_crush_model(loser, damage)
    result = loser.armor_curr
    assert result == expected_result


@pytest.mark.parametrize(
    "damage",
    [
        60,
        97,
        15.124,
        38.2,
        21.456,
        31,
        20,
        43,
        0.752,
    ],
)
def test_armor_crush_model_less(damage):
    loser = Character("Loser")
    loser.armor_curr = loser.armor
    armor_crush_model(loser, damage)
    result = loser.armor_curr
    assert result < loser.armor
