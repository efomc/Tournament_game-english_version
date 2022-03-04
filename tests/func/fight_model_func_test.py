import pytest
from tournament_game import (
    Character,
    fight_model,
)


@pytest.mark.parametrize(
    "number_of_fights, duelling_first, duelling_second, might, armor",
    [
        (1000, 51, 49, 20, 20),
        (1000, 39, 42, 20, 20),
        (1000, 95, 97, 20, 20),
        (1000, 68, 60, 20, 20),
    ],
)
def test_fight_model_duelling(
    number_of_fights, duelling_first, duelling_second, might, armor
):
    fighter1 = Character("first")
    fighter1.parameters = {
        "duelling": duelling_first,
        "might": might,
        "armor": armor,
    }
    fighter2 = Character("second")
    fighter2.parameters = {
        "duelling": duelling_second,
        "might": might,
        "armor": armor,
    }
    if fighter1.duelling > fighter2.duelling:
        expected_winner = fighter1
    else:
        expected_winner = fighter2
    expected_wins = 0
    for fight in range(number_of_fights):
        winner = fight_model(fighter1, fighter2)
        if winner == expected_winner:
            expected_wins += 1
    assert number_of_fights // 2 < expected_wins < number_of_fights


@pytest.mark.parametrize(
    "number_of_fights, might_high, name_high, duelling, armor, delta",
    [
        (1000, 60, "first", 20, 20, 40),
        (1000, 45, "second", 40, 20, 40),
        (1000, 97, "second", 60, 20, 40),
        (1000, 68, "first", 80, 20, 40),
    ],
)
def test_fight_model_might(
    number_of_fights, might_high, name_high, duelling, armor, delta
):
    out_fail = 0
    for test in range(1000):
        fighter1 = Character("first")
        fighter1.parameters = {
            "duelling": duelling,
            "armor": armor,
        }
        fighter2 = Character("second")
        fighter2.parameters = {
            "duelling": duelling,
            "armor": armor,
        }
        if fighter1.name == name_high:
            expected_winner = fighter1
            fighter1.parameters["might"] = might_high
            fighter2.parameters["might"] = might_high - delta
        else:
            expected_winner = fighter2
            fighter1.parameters["might"] = might_high - delta
            fighter2.parameters["might"] = might_high
        expected_wins = 0
        for fight in range(number_of_fights):
            winner = fight_model(fighter1, fighter2)
            if winner == expected_winner:
                expected_wins += 1
        if not number_of_fights // 2 < expected_wins < number_of_fights:
            out_fail += 1
    print("Число провалов на ", 5000, "равно", out_fail)
    assert out_fail <= 50


@pytest.mark.parametrize(
    "number_of_fights, armor_high, name_high, duelling, might, delta",
    [
        (1000, 55, "first", 20, 20, 15),
        (1000, 43, "second", 40, 20, 15),
        (1000, 97, "second", 60, 20, 15),
        (1000, 68, "first", 80, 20, 15),
        (1000, 55, "first", 60, 20, 15),
        (1000, 25, "second", 60, 40, 15),
        (1000, 97, "second", 60, 60, 15),
        (1000, 67, "second", 60, 80, 15),
    ],
)
def test_fight_model_armor(
    number_of_fights, armor_high, name_high, duelling, might, delta
):
    for test in range(1000):
        fighter1 = Character("first")
        fighter1.parameters = {
            "duelling": duelling,
            "might": might,
        }
        fighter2 = Character("second")
        fighter2.parameters = {
            "duelling": duelling,
            "might": might,
        }
        if fighter1.name == name_high:
            fighter1.parameters["armor"] = armor_high
            fighter2.parameters["armor"] = armor_high - delta
            expected_winner = fighter1
        else:
            fighter1.parameters["armor"] = armor_high - delta
            fighter2.parameters["armor"] = armor_high
            expected_winner = fighter2
        expected_wins = 0
        for fight in range(number_of_fights):
            winner = fight_model(fighter1, fighter2)
            if winner == expected_winner:
                expected_wins += 1
        assert number_of_fights // 2 < expected_wins < number_of_fights
