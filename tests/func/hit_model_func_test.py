import pytest
from tournament_game import (
    hit_model,
    Character,
    gauss_dice,
    DICE_FIGHT_LIMIT,
)


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling, strike_numbers",
    [
        (10, 20, 100),
        (90, 40, 10),
        (200, 70, 100),
        (70, 200, 100),
    ],
)
def test_hit_model_result(fighter1_duelling, fighter2_duelling, strike_numbers):
    result_numbers = 0
    max_parameter_wins = 0
    character1 = Character("Fighter 1")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("Fighter 2")
    character2.parameters["duelling"] = fighter2_duelling
    max_duelling = max(fighter1_duelling, fighter2_duelling)
    for strike in range(1, strike_numbers + 1):
        hit_result = hit_model(character1, character2, gauss_dice(DICE_FIGHT_LIMIT))
        if "strike" in hit_result:
            result_numbers += 1
            winner = hit_result["strike"][0]
            if winner.parameters["duelling"] == max_duelling:
                max_parameter_wins += 1
    assert max_parameter_wins > result_numbers / 2


@pytest.mark.parametrize(
    "strike_numbers",
    [
        10000,
    ],
)
def test_hit_model_result_kiss_2(strike_numbers):
    test_result = True
    for parameter in range(1, DICE_FIGHT_LIMIT):
        result_numbers = 0
        character1 = Character("Fighter 1")
        character1.parameters["duelling"] = parameter
        character2 = Character("Fighter 2")
        character2.parameters["duelling"] = DICE_FIGHT_LIMIT - parameter
        for strike in range(1, strike_numbers + 1):
            hit_result = hit_model(character1, character2, gauss_dice(DICE_FIGHT_LIMIT))
            if hit_result == "kiss":
                result_numbers += 1
            elif hit_result in ("compensation", "miss"):
                test_result = False
        if not result_numbers:
            test_result = False
    assert test_result


@pytest.mark.parametrize(
    "fighter1_duelling, fighter2_duelling, strike_numbers",
    [
        (80, 20, 10000),
        (90, 10, 10000),
        (31, 69, 10000),
        (24, 76, 10000),
        (2, 98, 10000),
        (1, 99, 10000),
        (99, 1, 10000),
    ],
)
def test_hit_model_result_kiss(fighter1_duelling, fighter2_duelling, strike_numbers):
    result_numbers = 0
    character1 = Character("Fighter 1")
    character1.parameters["duelling"] = fighter1_duelling
    character2 = Character("Fighter 2")
    character2.parameters["duelling"] = fighter2_duelling
    for strike in range(1, strike_numbers + 1):
        hit_result = hit_model(character1, character2, gauss_dice(DICE_FIGHT_LIMIT))
        if hit_result == "kiss":
            result_numbers += 1
    assert result_numbers >= 1


@pytest.mark.parametrize(
    "strike_numbers",
    [
        100,
    ],
)
def test_hit_model_result_not_strike_options(strike_numbers):
    kiss_result = False
    miss_result = False
    compensation_result = False
    for parameter1 in range(1, DICE_FIGHT_LIMIT):
        for parameter2 in range(1, DICE_FIGHT_LIMIT):
            character1 = Character("Fighter 1")
            character1.parameters["duelling"] = parameter1
            character2 = Character("Fighter 2")
            character2.parameters["duelling"] = parameter2
            for strike in range(1, strike_numbers + 1):
                hit_result = hit_model(
                    character1, character2, gauss_dice(DICE_FIGHT_LIMIT)
                )
                if hit_result == "kiss":
                    kiss_result = True
                elif hit_result == "miss":
                    miss_result = True
                elif hit_result == "compensation":
                    compensation_result = True
    assert kiss_result and miss_result and compensation_result


@pytest.mark.parametrize(
    "strike_numbers",
    [
        10000,
    ],
)
def test_hit_model_result_miss(strike_numbers):
    for parameter1 in range(1, DICE_FIGHT_LIMIT):
        for parameter2 in range(1, DICE_FIGHT_LIMIT):
            if parameter1 + parameter2 < DICE_FIGHT_LIMIT - 1:
                miss_numbers = 0
                character1 = Character("Fighter 1")
                character1.parameters["duelling"] = parameter1
                character2 = Character("Fighter 2")
                character2.parameters["duelling"] = parameter2
                for strike in range(1, strike_numbers + 1):
                    hit_result = hit_model(
                        character1, character2, gauss_dice(DICE_FIGHT_LIMIT)
                    )
                    if hit_result == "miss":
                        miss_numbers += 1
                print(parameter1, parameter2, miss_numbers)
                print(int(round((DICE_FIGHT_LIMIT - parameter1 - parameter2) / 10)))
                assert miss_numbers > round(
                    (DICE_FIGHT_LIMIT - parameter1 - parameter2) / 10
                )


@pytest.mark.parametrize(
    "strike_numbers",
    [
        10000,
    ],
)
def test_hit_model_result_compensation(strike_numbers):
    for parameter1 in range(1, DICE_FIGHT_LIMIT):
        for parameter2 in range(1, DICE_FIGHT_LIMIT):
            if parameter1 + parameter2 > DICE_FIGHT_LIMIT + 2:
                compensation_numbers = 0
                character1 = Character("Fighter 1")
                character1.parameters["duelling"] = parameter1
                character2 = Character("Fighter 2")
                character2.parameters["duelling"] = parameter2
                for strike in range(1, strike_numbers + 1):
                    hit_result = hit_model(
                        character1, character2, gauss_dice(DICE_FIGHT_LIMIT)
                    )
                    if hit_result == "compensation":
                        compensation_numbers += 1
                print(parameter1, parameter2, compensation_numbers)
                print(int(round((DICE_FIGHT_LIMIT - parameter1 - parameter2) / 10)))
                assert compensation_numbers > round(
                    (parameter1 + parameter2 - DICE_FIGHT_LIMIT - 1) / 10
                )
