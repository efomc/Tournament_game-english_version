import pytest
from tournament_game import get_winner, Character


@pytest.mark.parametrize("name", ["текст", "42", "", 12, -345, 52.08, None, True])
def test_get_winner_solo(name):
    character_sample = Character(name)
    character_list = [character_sample]
    assert str(name) == get_winner(character_list)


@pytest.mark.parametrize("name_list", [["текст", 42], ["", 1252.08]])
def test_get_winner_set(name_list):
    character_list = [Character(name) for name in name_list]
    assert name_list[0] == get_winner(character_list)


@pytest.mark.parametrize("name", ["текст", "42", "", 12, -345, 52.08, None, True])
def test_get_winner_type(name):
    character_sample = Character(name)
    character_list = [character_sample]
    name = get_winner(character_list)
    assert isinstance(name, str)
