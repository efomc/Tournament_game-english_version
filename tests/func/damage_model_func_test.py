import pytest
from tournament_game import (
    damage_model,
)


@pytest.mark.parametrize(
    "hit_strength",
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
def test_damage_model_value(hit_strength):
    result = damage_model(hit_strength)
    assert result >= hit_strength
