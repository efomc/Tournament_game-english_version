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
def test_armor_crush_model_type(damage):
    loser = Character("Loser")
    loser.armor_curr = 0
    armor_crush_model(loser, damage)
    assert isinstance(loser.armor_curr, int) or isinstance(loser.armor_curr, float)


@pytest.mark.parametrize("damage", [-139, -12.235, -0.000234])
def test_armor_crush_enter_wrong(damage):
    loser = Character("Loser")
    expected_result = 0
    loser.armor_curr = expected_result
    armor_crush_model(loser, damage)
    assert loser.armor_curr == expected_result
