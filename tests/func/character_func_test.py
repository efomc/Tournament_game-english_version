import builtins

import pytest
from random import randrange
from statistics import mean
from tournament_game import (
    Character,
    generate_characters,
    generate_name_list,
    PARAMETERS_DELTAS,
    CATEGORIES_LIMITS,
    GENERAL_NAME_LIST,
)


@pytest.mark.parametrize(
    "exam_numbers, roll_numbers,  confidence_interval, fail_percentage",
    [
        (1000, 100000, 5, 2),
    ],
)
def test_determ_parameter_func(
    exam_numbers, roll_numbers, confidence_interval, fail_percentage
):
    fighter = Character("Simple_name")
    par_type_list = list(PARAMETERS_DELTAS)
    par_base_list = list(CATEGORIES_LIMITS)
    fail_numbers = 0
    limit_fail_numbers = exam_numbers * fail_percentage / 100
    for exam in range(exam_numbers):
        par_type_index = randrange(0, len(par_type_list))
        par_base_index = randrange(0, len(par_base_list))
        par_type = par_type_list[par_type_index]
        par_base = par_base_list[par_base_index]
        low_limit, high_limit = CATEGORIES_LIMITS[par_base]
        deltas = PARAMETERS_DELTAS[par_type]
        delta = dict(zip(CATEGORIES_LIMITS, deltas))[par_base]
        range_value = high_limit - low_limit
        normal_frequency = (1 / range_value) * (1 + confidence_interval / 100)
        frequency_dict = {}
        for key in range(low_limit + delta, high_limit + delta):
            frequency_dict[key] = 0
        for roll in range(roll_numbers):
            exit_parameter = fighter.determ_parameter(par_type, par_base)
            frequency_dict[exit_parameter] += 1
        invert_frequency_dict = {frequency_dict[key]: key for key in frequency_dict}
        max_value = max(key for key in invert_frequency_dict)
        exit_frequency = max_value / roll_numbers
        if exit_frequency >= normal_frequency:
            fail_numbers += 1
    assert fail_numbers <= limit_fail_numbers


@pytest.mark.parametrize(
    "exam_numbers, characters_numbers,  confidence_interval, fail_percentage",
    [
        (100, 10000, 10, 1),
    ],
)
def test_generate_character_high_param(
    exam_numbers, characters_numbers, confidence_interval, fail_percentage
):
    base_index_dict = {}
    index = 0
    fail_numbers = 0
    limit_fail_numbers = exam_numbers * fail_percentage / 100
    for base in CATEGORIES_LIMITS:
        base_index_dict[base] = index
        index += 1
    for exam in range(exam_numbers):
        high_deviation_result = True
        parameter_deviation_result = True
        frequency_dict = {}
        for parameter in PARAMETERS_DELTAS:
            frequency_dict[parameter] = {}
            for base in CATEGORIES_LIMITS:
                frequency_dict[parameter][base] = 0
        for character_number in range(characters_numbers):
            fighter = Character("Simple_name")
            for parameter in fighter.parameters:
                for base in CATEGORIES_LIMITS:
                    base_index = base_index_dict[base]
                    limit_bottom = (
                        CATEGORIES_LIMITS[base][0]
                        + PARAMETERS_DELTAS[parameter][base_index]
                    )
                    limit_top = (
                        CATEGORIES_LIMITS[base][1]
                        + PARAMETERS_DELTAS[parameter][base_index]
                    )
                    if limit_bottom <= fighter.parameters[parameter] <= limit_top:
                        frequency_dict[parameter][base] += 1
        high_dict = {
            parameter: frequency_dict[parameter]["high"] for parameter in frequency_dict
        }
        high_deviation = percent_standard_deviation(high_dict)
        if high_deviation["relative deviation"] > confidence_interval:
            high_deviation_result = False
            print(
                'For "HIGH" - max category: ',
                high_deviation["max category"],
                "max deviation: ",
                high_deviation["max deviation"],
            )
        for parameter in frequency_dict:
            parameter_dict = frequency_dict[parameter]
            parameter_deviation = percent_standard_deviation(parameter_dict)
            if parameter_deviation["relative deviation"] > confidence_interval:
                parameter_deviation_result = False
                print(
                    f'For "{parameter}" - max category: ',
                    high_deviation["max category"],
                    "max deviation: ",
                    high_deviation["max deviation"],
                )
        if high_deviation_result is False or parameter_deviation_result is False:
            fail_numbers += 1
    assert fail_numbers <= limit_fail_numbers


def percent_standard_deviation(data_dict):
    data_list = (data_dict[key] for key in data_dict)
    average_value = mean(data_list)
    sum_of_square_deviation = 0
    deviation_dict = {}
    for key in data_dict:
        simple_deviation = data_dict[key] - average_value
        square_deviation = simple_deviation ** 2
        sum_of_square_deviation += square_deviation
        relative_deviation = simple_deviation * 100 / average_value
        deviation_dict[key] = relative_deviation
    standard_deviation = (sum_of_square_deviation / (len(data_dict) - 1)) ** 0.5
    percent_deviation = (standard_deviation / average_value) * 100
    inverce_deviation_dict = {abs(deviation_dict[key]): key for key in deviation_dict}
    max_value = max(inverce_deviation_dict)
    max_key = inverce_deviation_dict[max_value]
    return {
        "relative deviation": percent_deviation,
        "max category": max_key,
        "max deviation": deviation_dict[max_key],
    }


@pytest.mark.parametrize(
    "duelling_value",
    [
        0,
        12,
        -30,
        0.004,
        -0.462,
        149,
    ],
)
def test_character_duelling_property(duelling_value):
    fighter = Character("Simple_name")
    fighter.parameters["duelling"] = duelling_value
    assert fighter.duelling == duelling_value


@pytest.mark.parametrize(
    "might_value",
    [
        0,
        12,
        -30,
        0.004,
        -0.462,
        149,
    ],
)
def test_character_might_property(might_value):
    fighter = Character("Simple_name")
    fighter.parameters["might"] = might_value
    assert fighter.might == might_value


@pytest.mark.parametrize(
    "armor_value",
    [
        0,
        12,
        -30,
        0.004,
        -0.462,
        149,
    ],
)
def test_character_armor_property(armor_value):
    fighter = Character("Simple_name")
    fighter.parameters["armor"] = armor_value
    assert fighter.armor == armor_value


@pytest.mark.parametrize("numbers_of_characters", [10, 1, 10000])
def test_generate_characters(numbers_of_characters, monkeypatch):
    name_list = [
        tuple(["Name " + str(number)]) for number in range(numbers_of_characters)
    ]
    print(name_list)
    monkeypatch.setattr(
        "tournament_game.character.generate_name_list", lambda: name_list
    )
    characters_list = generate_characters()
    element_type_result = True
    element_name_result = True
    for index, element in enumerate(characters_list):
        if not isinstance(element, Character):
            element_type_result = False
        if element.name != name_list[index][0]:
            element_name_result = False
    assert (
        len(characters_list) == numbers_of_characters
        and element_type_result
        and element_name_result
    )


@pytest.mark.parametrize(
    "total_fighters_number, "
    "name, "
    "name_list, "
    "name_list_division, "
    "parameter_type, "
    "parameter_base",
    [
        (8, ["Test Name 1", None], None, "1", "duelling", "normal"),
        (
            4,
            [None],
            [
                ("Test Name 1", "armor", "high"),
                ("Test Name 2", "might", "low"),
                ("Test Name 3", "armor", "high"),
                ("Test Name 4", "might", "low"),
            ],
            "32",
            None,
            None,
        ),
        (16, ["Name", "Name", "Name", None], None, "3", None, None),
        (0, [None], None, "32", None, None),
    ],
)
def test_generate_name_list_func_complex(
    total_fighters_number,
    name,
    name_list,
    name_list_division,
    parameter_type,
    parameter_base,
    monkeypatch,
):
    expected_result = {
        "name list len": total_fighters_number,
        "Names format is str": total_fighters_number,
        "Parameter type from constant": total_fighters_number,
        "Parameter base from constant": total_fighters_number,
    }
    out_result = {
        "Names format is str": 0,
        "Parameter type from constant": 0,
        "Parameter base from constant": 0,
    }
    preset_names_number = len(name) - 1
    name_counter = iter(name)
    monkeypatch.setattr(
        "tournament_game.character.ask_for_fighters_number",
        lambda: total_fighters_number,
    )
    monkeypatch.setattr(
        "tournament_game.character.ask_for_name",
        lambda fighter_index: next(name_counter),
    )
    if name_list:
        monkeypatch.setattr(
            "tournament_game.character.choose_name_list",
            lambda fighter_number: name_list,
        )
        expected_result["preset name list in out"] = name_list
    monkeypatch.setattr(builtins, "input", lambda: name_list_division)
    monkeypatch.setattr(
        "tournament_game.character.ask_for_parameters",
        lambda request_name: (parameter_type, parameter_base),
    )
    if parameter_type and parameter_base:
        expected_result["preset names have preset parameters"] = preset_names_number
    else:
        expected_result["Parameter type from constant"] = (
            total_fighters_number - preset_names_number
        )
        expected_result["Parameter base from constant"] = (
            total_fighters_number - preset_names_number
        )

    out_name_list = generate_name_list()
    out_result["name list len"] = len(out_name_list)
    out_name_series = [item[0] for item in out_name_list]
    out_name_list_for_preset_names = out_name_list[:preset_names_number]
    expected_result["preset names series in out"] = name[:-1]
    out_result["preset names series in out"] = out_name_series[:preset_names_number]
    out_name_list_to_preset = out_name_list[preset_names_number:]
    if name_list:
        out_result["preset name list in out"] = out_name_list_to_preset
    else:
        expected_result["generated names from choosen General Name List in out"] = (
            total_fighters_number - preset_names_number
        )
        preset_names_division = set(name_list_division)
        character_in_preset_divisions = 0
        for character_set in out_name_list_to_preset:
            for names_division in preset_names_division:
                if (
                    character_set
                    in GENERAL_NAME_LIST[int(names_division) - 1].characters_sets
                ):
                    character_in_preset_divisions += 1
        out_result[
            "generated names from choosen General Name List in out"
        ] = character_in_preset_divisions
    if parameter_type and parameter_base:
        preset_parameters_for_preset_names = 0
        for character_set in out_name_list_for_preset_names:
            out_parameter_type, out_parameter_base = character_set[1:3]
            if (
                out_parameter_type == parameter_type
                and out_parameter_base == parameter_base
            ):
                preset_parameters_for_preset_names += 1
        out_result[
            "preset names have preset parameters"
        ] = preset_parameters_for_preset_names
    for character_set in out_name_list:
        out_name, out_parameter_type, out_parameter_base = character_set
        if isinstance(out_name, str):
            out_result["Names format is str"] += 1
        if out_parameter_type in PARAMETERS_DELTAS:
            out_result["Parameter type from constant"] += 1
        if out_parameter_base in CATEGORIES_LIMITS:
            out_result["Parameter base from constant"] += 1
    assert out_result == expected_result
