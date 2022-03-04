import pytest
from tournament_game import (
    Character,
    strike_model,
)


def test_strike_model_simple():
    for strike in range(1, 10):
        fighter1 = Character("first")
        fighter1.armor_curr = fighter1.armor
        fighter2 = Character("second")
        fighter2.armor_curr = fighter2.armor
        strike_model(fighter1, fighter2, strike)


@pytest.mark.parametrize(
    "parameter",
    [
        "",
        "text",
        "32",
        "-0.1322",
    ],
)
def test_strike_model_error(parameter):
    with pytest.raises(TypeError):
        for strike in range(10):
            fighter1 = Character("first")
            fighter1.armor_curr = parameter
            fighter2 = Character("second")
            fighter2.armor_curr = fighter2.armor
            strike_model(fighter1, fighter2, strike)


def test_strike_model_print_dice(capfd):
    fighter1 = Character("first")
    fighter1.armor_curr = fighter1.armor
    fighter2 = Character("second")
    fighter2.armor_curr = fighter2.armor
    strike_model(fighter1, fighter2, strike_number=1)
    out = capfd.readouterr()[0]
    assert "Бросок на" in out


@pytest.mark.parametrize(
    "dice",
    [
        50,
        -20,
    ],
)
def test_strike_model_print_strike_dice(dice, monkeypatch, capfd):
    monkeypatch.setattr("tournament_game.fight.gauss_dice", lambda _: dice)
    fighter1 = Character("first")
    fighter1.armor_curr = fighter1.armor
    fighter2 = Character("second")
    fighter2.armor_curr = fighter2.armor
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert f"Бросок на {dice}" in out


@pytest.mark.parametrize(
    "winner_number",
    [
        2,
        1,
        1,
        2,
    ],
)
def test_strike_model_print_strike_descr_strike(winner_number, monkeypatch, capfd):
    fighter1 = Character("first")
    fighter1.armor_curr = fighter1.armor
    fighter2 = Character("second")
    fighter2.armor_curr = fighter2.armor
    fighters = [fighter1, fighter2]
    winner = fighters.pop(winner_number - 1)
    loser = fighters.pop()
    monkeypatch.setattr(
        "tournament_game.fight.hit_model",
        lambda par1, par2, par3: {"strike": (winner, loser)},
    )
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert f"Цели достиг удар бойца {winner.name}" in out


@pytest.mark.parametrize(
    "damage, winner_number, loser_armor_curr_result",
    [
        (20, 2, 1),
        (2, 1, 89),
        (140, 1, 20),
        (12.4, 2, 43.1),
    ],
)
def test_strike_model_print_strike_result_descr(
    damage, winner_number, loser_armor_curr_result, monkeypatch, capfd
):
    fighter1 = Character("first")
    fighter1.armor_curr = fighter1.armor
    fighter2 = Character("second")
    fighter2.armor_curr = fighter2.armor
    fighters = [fighter1, fighter2]
    winner = fighters.pop(winner_number - 1)
    loser = fighters.pop()
    monkeypatch.setattr(
        "tournament_game.fight.hit_model",
        lambda par1, par2, par3: {"strike": (winner, loser)},
    )
    monkeypatch.setattr("tournament_game.fight.damage_model", lambda par1: damage)
    monkeypatch.setattr(
        "tournament_game.fight.armor_crush_model",
        lambda par1, par2: loser_armor_curr_result,
    )
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert (
        f"Он нанес урон на {damage}.\nБроня бойца {loser.name} теперь {loser.armor_curr}"
        in out
    )


def test_strike_model_print_strike_descr_miss(monkeypatch, capfd):
    fighter1 = Character("first")
    fighter2 = Character("second")
    monkeypatch.setattr(
        "tournament_game.fight.hit_model", lambda par1, par2, par3: "miss"
    )
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert f"Оба промахнулись. Бьют снова!" in out


def test_strike_model_print_strike_descr_compensation(monkeypatch, capfd):
    fighter1 = Character("first")
    fighter2 = Character("second")
    monkeypatch.setattr(
        "tournament_game.fight.hit_model", lambda par1, par2, par3: "compensation"
    )
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert f"Удар парирован!" in out


def test_strike_model_print_strike_descr_kiss(monkeypatch, capfd):
    fighter1 = Character("first")
    fighter2 = Character("second")
    monkeypatch.setattr(
        "tournament_game.fight.hit_model", lambda par1, par2, par3: "kiss"
    )
    strike_model(fighter1, fighter2, 1)
    out = capfd.readouterr()[0]
    assert f"Они целуются! Но вот бьют снова!" in out
