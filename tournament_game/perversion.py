from random import shuffle, randrange
from typing import Optional

from tournament_game.constants import UNRELIABLE_LIMIT


# defines the best/worst character stat. With the probability given
# by the UNRELIABLE_LIMIT constant, it will give erroneous data to mislead the user.
# определяет лучший/худший параметр персонажа. С вероятностью, заданной константой UNRELIABLE_LIMIT
# даст ошибочные данные, для введения пользователя в заблуждение.
def get_extremum_parameter(
    parameters: dict, best_parameter: str, worse_parameter: Optional[str] = None
):
    parameters_names = list(parameters)
    parameters_names.remove(best_parameter)
    if worse_parameter:
        parameters_names.remove(worse_parameter)
    else:
        shuffle(parameters_names)

    shuffle(parameters_names)
    fake = randrange(1, 101)

    if fake < UNRELIABLE_LIMIT:
        return parameters_names[0]

    if worse_parameter:
        return worse_parameter

    return best_parameter


# returns the worse parameter using the get_extremum_parameter function
# возвращает худший параметр с помощью функции get_extremum_parameter
def get_worse_parameter(
    parameters: dict, best_parameter: str, worse_parameter: str
) -> str:
    return get_extremum_parameter(parameters, best_parameter, worse_parameter)


# returns the best parameter using the get_extremum_parameter function
# возвращает лучший параметр с помощью функции get_extremum_parameter
def get_best_parameter(parameters: dict, best_parameter: str) -> str:
    return get_extremum_parameter(parameters, best_parameter)
