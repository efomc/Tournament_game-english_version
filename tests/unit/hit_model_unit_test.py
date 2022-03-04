import pytest
from tournament_game import hit_model, Character, gauss_dice, DICE_FIGHT_LIMIT


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling",
    [
        (10, 20),
        (90, 40),
        (-10, -100),
        (-90, 10),
        (200, 70),
    ],
)
def test_hit_model_unit_fact(fighter1_duelling, fighter2_duelling):
    character1 = Character("Fighter 1")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("Fighter 2")
    character2.parameters["duelling"] = fighter2_duelling
    hit_model(character1, character2, gauss_dice(100))


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling, dice, winner",
    [
        (10, 20, 5, "first"),
        (90, 40, 92, "second"),
        (10, 30, 79, "second"),
        (60, 75, 21, "first"),
        (80, 70, 88, "second"),
    ],
)
def test_hit_model_unit_strike(fighter1_duelling, fighter2_duelling, dice, winner):
    character1 = Character("first")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("second")
    character2.parameters["duelling"] = fighter2_duelling
    assert winner == hit_model(character1, character2, dice)["strike"][0].name


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling, dice",
    [
        (65, 41, 65),
        (98, 82, 18),
        (55, 55, 50),
        (68, 64, 62),
        (71, 30, 71),
        (71, 30, 70),
    ],
)
def test_hit_model_unit_compensation(fighter1_duelling, fighter2_duelling, dice):
    character1 = Character("first")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("second")
    character2.parameters["duelling"] = fighter2_duelling
    assert "compensation" == hit_model(character1, character2, dice)


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling, dice",
    [
        (60, 31, 61),
        (97, 1, 98),
        (15, 75, 20),
        (38, 34, 62),
        (21, 30, 50),
        (31, 20, 43),
    ],
)
def test_hit_model_unit_miss(fighter1_duelling, fighter2_duelling, dice):
    character1 = Character("first")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("second")
    character2.parameters["duelling"] = fighter2_duelling
    assert "miss" == hit_model(character1, character2, dice)


def test_hit_model_unit_kiss():
    for fighter1_duelling in range(1, DICE_FIGHT_LIMIT):
        character1 = Character("first")
        character1.parameters["duelling"] = fighter1_duelling
        character2 = Character("second")
        character2.parameters["duelling"] = DICE_FIGHT_LIMIT - fighter1_duelling
        assert "kiss" == hit_model(character1, character2, fighter1_duelling)


def test_hit_model_unit_total_cover():
    for fighter1_duelling in range(1, DICE_FIGHT_LIMIT - 1):
        for fighter2_duelling in range(1, DICE_FIGHT_LIMIT - 1):
            character1 = Character("first")
            character1.parameters["duelling"] = fighter1_duelling
            character2 = Character("second")
            character2.parameters["duelling"] = fighter2_duelling
            for dice in range(1, DICE_FIGHT_LIMIT):
                comment = (
                    f"Fighter1 duelling = {fighter1_duelling},"
                    f"Fighter2 duelling = {fighter2_duelling}, dice = {dice}"
                )
                check_winner = True
                winner_result = hit_model(character1, character2, dice)
                if "strike" in winner_result:
                    winner_result = winner_result["strike"][0].name
                if fighter1_duelling + fighter2_duelling < DICE_FIGHT_LIMIT:
                    if dice <= fighter1_duelling:
                        check_winner = "first"
                    elif (
                        fighter1_duelling < dice < DICE_FIGHT_LIMIT - fighter2_duelling
                    ):
                        check_winner = "miss"
                    elif DICE_FIGHT_LIMIT - fighter2_duelling <= dice:
                        check_winner = "second"
                elif fighter1_duelling + fighter2_duelling == DICE_FIGHT_LIMIT:
                    if dice < fighter1_duelling:
                        check_winner = "first"
                    elif (
                        fighter1_duelling
                        == dice
                        == DICE_FIGHT_LIMIT - fighter2_duelling
                    ):
                        check_winner = "kiss"
                    elif dice > DICE_FIGHT_LIMIT - fighter2_duelling:
                        check_winner = "second"
                elif fighter1_duelling + fighter2_duelling > DICE_FIGHT_LIMIT:
                    if dice < DICE_FIGHT_LIMIT - fighter2_duelling:
                        check_winner = "first"
                    elif (
                        DICE_FIGHT_LIMIT - fighter2_duelling
                        <= dice
                        <= fighter1_duelling
                    ):
                        check_winner = "compensation"
                    elif fighter1_duelling < dice:
                        check_winner = "second"
                assert (winner_result, comment) == (check_winner, comment)
