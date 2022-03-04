import pytest
from tournament_game import (
    damage_model,
)


@pytest.mark.parametrize(
    "hit_strength",
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
def test_damage_model_type(hit_strength):
    result = damage_model(hit_strength)
    assert isinstance(result, int) or isinstance(result, float)


@pytest.mark.parametrize(
    "hit_strength",
    [
        0,
        0.0123,
        4,
        0.42,
        60,
        97,
        15,
        38.23,
        21,
        31,
        20,
        43.123,
        1345,
    ],
)
def test_damage_model_abs(hit_strength):
    result = damage_model(hit_strength)
    assert result >= 0


@pytest.mark.parametrize("hit_strength", ["текст", "42", "", -139, -12.235, -0.000234])
def test_damage_model_enter_wrong(hit_strength):
    result = damage_model(hit_strength)
    assert not result
