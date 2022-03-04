import builtins

import pytest
from tournament_game import yes_no


@pytest.mark.parametrize(
    "question, answers, ultimate_outcome",
    [
        (None, ["Yes"], True),
        (None, ["No_mean_input", "123", "0"], False),
        (None, ["YEAPPP", "YeP"], True),
    ],
)
def test_yes_no_func_complex(question, answers, ultimate_outcome, monkeypatch):
    expected_result = {
        "type of function return": True,
        "data return": ultimate_outcome,
    }
    answers = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda par1=question: next(answers))
    yes_no_result = yes_no(str(question))
    out_result = {
        "type of function return": isinstance(yes_no_result, bool),
        "data return": yes_no_result,
    }

    assert out_result == expected_result
