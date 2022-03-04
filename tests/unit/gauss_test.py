import pytest
from tournament_game import gauss_dice


@pytest.mark.parametrize("parameter", ["текст", "42", ""])
def test_gauss_enter_type(parameter):
    with pytest.raises(TypeError) or pytest.raises(ValueError):
        gauss_dice(parameter)


@pytest.mark.parametrize(
    "parameter", [0, 0.22, 1, 3, 10, 17, 50, 92, 100, 487, 1329, -30, -78000]
)
def test_gauss_type(parameter):
    dice = gauss_dice(parameter)
    assert isinstance(dice, int) or isinstance(dice, float)


@pytest.mark.parametrize(
    "parameter", [0, 1, 3, 10, 17, 50, 92, 100, 487, 1329, -30, -78000]
)
def test_gauss_limits(parameter):
    for roll in range(10000):
        dice = gauss_dice(parameter)
        if parameter >= 0:
            result = 0 <= dice <= parameter
        else:
            result = parameter <= dice <= 0
        assert result


@pytest.mark.parametrize("parameter", [3, 10, 17, 50, 92, 100, 487, 1329, -30, -78000])
def test_gauss_kurtosis(
    parameter,
):  # проверяет нормальность распределения и остроту пика
    roll_numbers = 1000
    result_25 = 0
    for roll in range(roll_numbers):
        roll_result = gauss_dice(parameter)
        if (
            abs(parameter * (0.5 - 0.25))
            <= abs(roll_result)
            <= abs(parameter * (0.5 + 0.25))
        ):
            result_25 += 1
    covariance = round(100 * result_25 / roll_numbers)
    assert covariance >= 65
