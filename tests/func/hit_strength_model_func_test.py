import pytest
from tournament_game import (
    hit_strength_model,
    Character,
)


@pytest.mark.parametrize(
    "strength",
    [
        1,
        0.85,
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
def test_hit_strenght_limits(strength):
    fighter = Character("Fighter")
    fighter.parameters["might"] = strength
    for hit in range(1000):
        result = hit_strength_model(fighter)
        assert 0 <= result <= strength


@pytest.mark.parametrize(
    "strength",
    [
        1,
        0.85,
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
def test_hit_strenght_kurtosis(strength):
    result_25 = 0
    hit_numbers = 1000
    fighter = Character("Fighter")
    fighter.parameters["might"] = strength
    for hit in range(hit_numbers):
        result = hit_strength_model(fighter)
        if abs(strength * (0.5 - 0.25)) <= abs(result) <= abs(strength * (0.5 + 0.25)):
            result_25 += 1
    covariance = round(100 * result_25 / hit_numbers)
    assert covariance >= 65
