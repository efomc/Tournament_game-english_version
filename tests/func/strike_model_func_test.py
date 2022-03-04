import pytest
from tournament_game import (
    Character,
    strike_model,
)


def test_strike_model_common():
    fighter1 = Character("first")
    fighter1.armor_curr = fighter1.armor
    fighter2 = Character("second")
    fighter2.armor_curr = fighter2.armor
    for strike in range(1, 10):
        strike_model(fighter1, fighter2, strike)
    assert (
        fighter1.armor_curr != fighter1.armor or fighter2.armor_curr != fighter1.armor
    )


@pytest.mark.parametrize(
    "numbers_of_fights, limit_of_strikes",
    [
        (10000, 150),
    ],
)
def test_strike_model_long(numbers_of_fights, limit_of_strikes):
    for fight in range(numbers_of_fights):
        fighter1 = Character("first")
        fighter1.armor_curr = fighter1.armor
        fighter2 = Character("second")
        fighter2.armor_curr = fighter2.armor
        strike_number = 0
        while fighter1.armor_curr > 0 and fighter2.armor_curr > 0:
            strike_number += 1
            strike_model(fighter1, fighter2, strike_number)
        assert strike_number <= limit_of_strikes


@pytest.mark.parametrize(
    "numbers_of_fights, limit_of_strikes, percent_limit_strikes",
    [
        (10000, 10, 0.8),
    ],
)
def test_strike_model_percent_long(
    numbers_of_fights, limit_of_strikes, percent_limit_strikes
):
    numbers_of_good_long = 0
    for fight in range(numbers_of_fights):
        fighter1 = Character("first")
        fighter1.armor_curr = fighter1.armor
        fighter2 = Character("second")
        fighter2.armor_curr = fighter2.armor
        strike_number = 0
        while fighter1.armor_curr > 0 and fighter2.armor_curr > 0:
            strike_number += 1
            strike_model(fighter1, fighter2, strike_number)
        if strike_number <= limit_of_strikes:
            numbers_of_good_long += 1
    assert numbers_of_good_long / numbers_of_fights >= percent_limit_strikes


@pytest.mark.parametrize(
    "numbers_of_fights",
    [
        50,
    ],
)
def test_strike_model_print_strike_description(numbers_of_fights, capfd, monkeypatch):
    result_dict = {
        "Цели достиг удар бойца first": False,
        "Цели достиг удар бойца second": False,
        "Они целуются! Но вот бьют снова!": False,
        "Удар парирован!": False,
        "Оба промахнулись. Бьют снова!": False,
    }

    expected_result_dict = {
        "Цели достиг удар бойца first": True,
        "Цели достиг удар бойца second": True,
        "Они целуются! Но вот бьют снова!": True,
        "Удар парирован!": True,
        "Оба промахнулись. Бьют снова!": True,
    }
    for fight in range(numbers_of_fights):
        fighter1 = Character("first")
        fighter1.armor_curr = fighter1.armor
        fighter2 = Character("second")
        fighter2.armor_curr = fighter2.armor
        strike_model(fighter1, fighter2, strike_number=1)
        out = capfd.readouterr()[0]
        for key in result_dict:
            if key in out:
                result_dict[key] = True
    if not result_dict["Они целуются! Но вот бьют снова!"]:
        monkeypatch.setattr(
            "tournament_game.fight.hit_model", (lambda fighter1, fighter2, dice: "kiss")
        )
        fighter1 = Character("first")
        fighter2 = Character("second")
        strike_model(fighter1, fighter2, 1)
        out = capfd.readouterr()[0]
        if "Они целуются! Но вот бьют снова!" in out:
            result_dict["Они целуются! Но вот бьют снова!"] = True
    assert result_dict == expected_result_dict
