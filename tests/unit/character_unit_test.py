import pytest
from tournament_game import (
    Character,
    CATEGORIES_LIMITS,
    PARAMETERS_DELTAS,
)


def test_character_init():
    fighter1 = Character("Simple_name")
    assert (
        isinstance(fighter1, Character)
        and fighter1.name == "Simple_name"
        and fighter1.armor
        and fighter1.duelling
        and fighter1.might
    )


def test_character_param_limit():
    for effort in range(100):
        fighter1 = Character("Simple_name")
        categories_set = set()
        expected_categories_set = {"low", "normal", "high"}
        for parameter in fighter1.parameters:
            low_limit_bottom = (
                CATEGORIES_LIMITS["low"][0] + PARAMETERS_DELTAS[parameter][0]
            )
            low_limit_top = (
                CATEGORIES_LIMITS["low"][1] + PARAMETERS_DELTAS[parameter][0]
            )
            normal_limit_bottom = (
                CATEGORIES_LIMITS["normal"][0] + PARAMETERS_DELTAS[parameter][1]
            )
            normal_limit_top = (
                CATEGORIES_LIMITS["normal"][1] + PARAMETERS_DELTAS[parameter][1]
            )
            high_limit_bottom = (
                CATEGORIES_LIMITS["high"][0] + PARAMETERS_DELTAS[parameter][2]
            )
            high_limit_top = (
                CATEGORIES_LIMITS["high"][1] + PARAMETERS_DELTAS[parameter][2]
            )
            if high_limit_bottom <= fighter1.parameters[parameter] <= high_limit_top:
                categories_set.add("high")
            elif (
                normal_limit_bottom
                <= fighter1.parameters[parameter]
                <= normal_limit_top
            ):
                categories_set.add("normal")
            elif low_limit_bottom <= fighter1.parameters[parameter] <= low_limit_top:
                categories_set.add("low")
        assert categories_set == expected_categories_set


@pytest.mark.parametrize(
    "parameter_type, parameter_category",
    [
        ("duelling", "low"),
        ("might", "high"),
        ("duelling", "normal"),
        ("armor", "normal"),
        ("might", "low"),
    ],
)
def test_character_param_determ(parameter_type, parameter_category):
    fighter1 = Character("Simple_name", parameter_type, parameter_category)
    categories_set = set()
    expected_categories_set = {"low", "normal", "high"}
    parameters = {}
    for parameter in fighter1.parameters:
        low_limit_bottom = CATEGORIES_LIMITS["low"][0] + PARAMETERS_DELTAS[parameter][0]
        low_limit_top = CATEGORIES_LIMITS["low"][1] + PARAMETERS_DELTAS[parameter][0]
        normal_limit_bottom = (
            CATEGORIES_LIMITS["normal"][0] + PARAMETERS_DELTAS[parameter][1]
        )
        normal_limit_top = (
            CATEGORIES_LIMITS["normal"][1] + PARAMETERS_DELTAS[parameter][1]
        )
        high_limit_bottom = (
            CATEGORIES_LIMITS["high"][0] + PARAMETERS_DELTAS[parameter][2]
        )
        high_limit_top = CATEGORIES_LIMITS["high"][1] + PARAMETERS_DELTAS[parameter][2]
        if high_limit_bottom <= fighter1.parameters[parameter] <= high_limit_top:
            categories_set.add("high")
            parameters[parameter] = "high"
        elif normal_limit_bottom <= fighter1.parameters[parameter] <= normal_limit_top:
            categories_set.add("normal")
            parameters[parameter] = "normal"
        elif low_limit_bottom <= fighter1.parameters[parameter] <= low_limit_top:
            categories_set.add("low")
            parameters[parameter] = "low"
    assert (
        parameters[parameter_type] == parameter_category
        and categories_set == expected_categories_set
    )


@pytest.mark.parametrize(
    "efforts_nubmers",
    [
        100,
    ],
)
def test_character_gen_armor_curr(efforts_nubmers):
    for effort in range(efforts_nubmers):
        fighter1 = Character("Simple_name")
        assert not fighter1.armor_curr


@pytest.mark.parametrize(
    "par_type, par_base",
    [
        ("duelling", "low"),
        ("might", "high"),
        ("duelling", "normal"),
        ("armor", "normal"),
        ("might", "low"),
    ],
)
def test_determ_parameter_direct(par_type, par_base):
    fighter = Character("Simple_name")
    base_index_dict = {
        "low": 0,
        "normal": 1,
        "high": 2,
    }
    base_index = base_index_dict[par_base]
    limit_bottom = (
        CATEGORIES_LIMITS[par_base][0] + PARAMETERS_DELTAS[par_type][base_index]
    )
    limit_top = CATEGORIES_LIMITS[par_base][1] + PARAMETERS_DELTAS[par_type][base_index]
    exit_parameter = fighter.determ_parameter(par_type, par_base)
    assert (
        isinstance(exit_parameter, int) and limit_bottom <= exit_parameter <= limit_top
    )
