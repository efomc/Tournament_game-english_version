import pytest
from tournament_game import (
    hit_strength_model,
    Character,
)


@pytest.mark.parametrize(
    "strength",
    [
        60,
        97,
        15,
        38,
        21,
        31,
        20,
        43,
    ],
)
def test_hit_strength_type(strength):
    fighter = Character("Fighter")
    fighter.parameters["might"] = strength
    result = hit_strength_model(fighter)
    assert isinstance(result, int) or isinstance(result, float)


@pytest.mark.parametrize(
    "strength",
    [
        60,
        97,
        15,
        38,
        21,
        31,
        20,
        43,
    ],
)
def test_hit_strength_abs(strength):
    fighter = Character("Fighter")
    fighter.parameters["might"] = strength
    result = hit_strength_model(fighter)
    assert result >= 0


@pytest.mark.parametrize(
    "parameter", ["текст", "42", "", 23, -139, 0, 23.58, -12.235, 0.000234]
)
def test_hit_strength_enter_type(parameter):
    with pytest.raises(AttributeError):
        hit_strength_model(parameter)


@pytest.mark.parametrize("strength", [-139, -12.235, -0.000234, 0])
def test_hit_strength_enter_negative(strength):
    fighter = Character("Fighter")
    fighter.parameters["might"] = strength
    result = hit_strength_model(fighter)
    assert not result
