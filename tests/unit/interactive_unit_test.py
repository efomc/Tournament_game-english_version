import builtins

import pytest
from tournament_game import (
    yes_no,
    ANSWER_OPTIONS_YES_NO,
    ERROR_OPTIONS_YES_NO,
)


@pytest.mark.parametrize(
    "question, "
    "answers, "
    "ultimate_outcome, "
    "positive_answers, "
    "negative_answers, "
    "error_message",
    [
        (
            "Question1",
            ("no variant", "Correct VAriaNt"),
            True,
            ("correct variant",),
            ("2",),
            ("very bad variant, return",),
        ),
        (
            "",
            (
                "wrong variant",
                "nO",
            ),
            False,
            None,
            None,
            None,
        ),
        ("Any question", ("YeP",), True, None, None, None),
        (
            "Any question",
            (
                "YePpppie",
                "nOPppapppas",
            ),
            False,
            None,
            (
                "no variant1",
                "no variant2",
                "nopppapppas",
            ),
            None,
        ),
        ("Any question", ("",), None, None, None, None),
        (
            "",
            ("", "any answer", "any incorrect answer"),
            None,
            ("1",),
            ("0",),
            ("This answer is incorrect",),
        ),
    ],
)
def test_yes_no_unit_complex(
    question,
    answers,
    ultimate_outcome,
    positive_answers,
    negative_answers,
    error_message,
    capfd,
    monkeypatch,
):
    stop_iteration_rised = False
    if not error_message:
        error_message = ERROR_OPTIONS_YES_NO[: len(answers) - 1]
    if not positive_answers:
        positive_answers = ANSWER_OPTIONS_YES_NO[0]
    if not negative_answers:
        negative_answers = ANSWER_OPTIONS_YES_NO[1]
    error_string = "\n".join(error_message)
    if error_string:
        error_string += "\n"
    if len(answers) - 1 > len(error_message):
        error_string += (error_message[-1] + "\n") * (
            len(answers) - 1 - len(error_message)
        )
    expected_result = {
        "question in out": True,
        "all error message in out": True,
        "all out": question + "\n" + error_string,
        "ultimate outcome is": ultimate_outcome,
    }
    answers = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda par1=question: next(answers))
    answer_options = (positive_answers, negative_answers)
    for answer in answers:
        if answer not in positive_answers + negative_answers:
            stop_iteration_rised = True
    if stop_iteration_rised:
        with pytest.raises(StopIteration):
            yes_no(question, answer_options, error_message)
    else:
        outcome = yes_no(question, answer_options, error_message)
        message_out = capfd.readouterr()[0]

        out_result = {
            "question in out": question + "\n" in message_out,
            "all error message in out": error_string in message_out,
            "all out": message_out,
            "ultimate outcome is": outcome,
        }

        assert out_result == expected_result
