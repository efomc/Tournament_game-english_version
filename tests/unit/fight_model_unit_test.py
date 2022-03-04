import pytest
from tournament_game import (
    Character,
    fight_model,
)


def test_fight_model_simple():
    fighter1 = Character("first")
    fighter2 = Character("second")
    assert fight_model(fighter1, fighter2)


def test_fight_model_type():
    fighter1 = Character("first")
    fighter2 = Character("second")
    winner = fight_model(fighter1, fighter2)
    assert isinstance(winner, Character)


@pytest.mark.parametrize(
    "numbers_of_fights",
    [
        1000,
    ],
)
def test_fight_model_print(numbers_of_fights, capfd, monkeypatch):
    fighter1 = Character("first")
    fighter2 = Character("second")
    monkeypatch.setattr(
        "tournament_game.fight.strike_model",
        lambda par1, par2, par3: armor_decrease(fighter1, -200),
    )
    fight_model(fighter1, fighter2)
    out = capfd.readouterr()[0]
    assert f"Победил second!\n" in out


def test_fight_model_winner(monkeypatch):
    fighter1 = Character("first")
    fighter2 = Character("second")
    monkeypatch.setattr(
        "tournament_game.fight.strike_model",
        lambda par1, par2, par3: armor_decrease(fighter2, -100),
    )
    winner = fight_model(fighter1, fighter2)
    assert winner == fighter1


def armor_decrease(fighter, value):
    fighter.armor_curr = value
