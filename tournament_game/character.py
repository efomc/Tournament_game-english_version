from random import shuffle, randrange
from typing import List, Tuple, Optional

from tournament_game.constants import CATEGORIES_LIMITS, PARAMETERS_DELTAS
from tournament_game.interactive import (
    ask_for_fighters_number,
    ask_for_name,
    ask_for_parameters,
    choose_name_list,
)


# class for describing and operating of fighters
# класс для описания бойцов и оперирования ими
class Character:
    def __init__(
        self,
        name: str,
        parameter_type: Optional[str] = None,
        parameter_category: Optional[str] = None,
    ):
        self.name = str(name)
        self.armor_curr = None
        self.parameters = {}

        # To ensure a balance between the fighters, only one of the parameters can have
        # a high score, one medium and one low.
        # To create a character, you can specify at most one parameter in the form -
        # parameter type (parameter_type from PARAMETERS_DELTAS) and value category
        # (parameter_category from CATEGORIES_LIMITS). From the set of parameter types
        # and categories, the specified values are excluded, the rest are distributed randomly.
        # If no parameters are given, the entire distribution is given randomly.
        # Since different parameters affect the results of the battle in different ways,
        # different corrections are used for the magnitude categories for different types
        # of parameters (PARAMETERS_DELTAS).
        # Для обеспечения баланса между бойцами, лишь один из параметров может иметь самый высокий
        # показатель, один средний и один низкий.
        # Для создания персонажа можно задать не более одного параметра в виде - тип параметра
        # (parameter_type из PARAMETERS_DELTAS) и категория величины (parameter_category из
        # CATEGORIES_LIMITS). Из набора типа параметров и категорий величины исключаются заданные,
        # остальные распределяются случайным образом.
        # Если не задан ни один параметр, все распределение задается случайным образом.
        # Поскольку разные параметры по-разному сказываются на результатах боя,
        # к категориям величины для разных типов параметров используются разные поправки
        # (PARAMETERS_DELTAS).
        parameter_category_set = set(CATEGORIES_LIMITS)
        if parameter_category in parameter_category_set:
            parameter_category_set.remove(parameter_category)

        parameter_category_list = list(parameter_category_set)
        shuffle(parameter_category_list)

        for par_type in PARAMETERS_DELTAS:
            if par_type == parameter_type:
                par_category = parameter_category
            else:
                par_category = parameter_category_list.pop()

            self.parameters[par_type] = self.determ_parameter(par_type, par_category)

        # determining the best and worst parameters for describing fighters
        # определение лучшего и худшего параметров для описания бойцов
        self.best_parameter = max(self.parameters, key=self.parameters.get)
        self.worse_parameter = min(self.parameters, key=self.parameters.get)

    # determine the value of the parameter: randomly within the interval for each value category
    # of each parameter
    # определяем значение параметра: случайным образом в пределах интервала
    # для каждой категории величины каждого параметра
    @staticmethod
    def determ_parameter(par_type: str, par_base: str) -> int:
        low_limit, high_limit = CATEGORIES_LIMITS[par_base]
        deltas = PARAMETERS_DELTAS[par_type]
        delta = dict(zip(CATEGORIES_LIMITS, deltas))[par_base]
        return randrange(low_limit + delta, high_limit + delta)

    @property
    def duelling(self):
        return self.parameters.get("duelling", 0)

    @property
    def might(self):
        return self.parameters.get("might", 0)

    @property
    def armor(self):
        return self.parameters.get("armor", 0)


# generating a list of fighters. The list items are fully generated characters
# of the Character class. When filling the list, characters are created based on
# the given parameter (one for each fighter) in the list of names (name_list).
# генерируем список бойцов. Элементы списка - полностью сгенеренные персонажи класса Character.
# При наполнении списка персонажи создаются на основе заданного параметра
# (одного для каждого бойца) в списке имен (name_list).
def generate_characters() -> List[Character]:
    name_list = generate_name_list()
    return [Character(*character_set) for character_set in name_list]


# Generation a list of names and specified parameters for fighters:
# 1. the user sets the total number of fighters from a given number of options
# (MULTIPLIC_BET_TOURN_WINNER),
# 2. the user chooses whether to create his fighters - give a name, if given a name,
# then set one parameter. If it refuses to set a parameter, they are set to None and
# are randomly assigned during character creation. If the user refuses to set options,
# the user is prompted to set the name of the next fighter.
# As soon as the user refuses to give a name, he is prompted to select sets of given names,
# from which the rest of the fighters will be randomly selected up to
# a given number of participants. At the output, we get a list from the character creation set:
# Name (name), given parameter (parameter_type),
# value category for the given parameter (parameter_base).
# создание списка имен и заданных параметров для бойцов:
# 1. пользователь задает общее число бойцов из заданного числа вариантов
# (MULTIPLIC_BET_TOURN_WINNER),
# 2. пользователь выбирает, будет ли создавать своих бойцов - дать имя, если дать имя,
# то задать один параметр. Если отказывается задать параметр,
# они задаются как None и при создании персонажа задаются случайным образом.
# Если пользователь отказыавется задать параметры, пользователю предлагается задать имя
# следующего бойца. Как только пользователь отказывается задавать имя,
# ему предлагается выбрать наборы заданных имен,
# из которых случайным образом будут отобраны остальные бойцы до заданного числа участников.
# На выходе получаем список из набора для создания персонажа:
# Имя (name), заданный параметр (parameter_type),
# категория величины для заданного параметра (parameter_base).
def generate_name_list() -> List[Tuple[str, str, str]]:
    name_list = []
    total_fighters_number = ask_for_fighters_number()
    for fighter_index in range(total_fighters_number):
        name = ask_for_name(fighter_index)

        if not name:
            fighters_number = total_fighters_number - fighter_index
            name_list.extend(choose_name_list(fighters_number))
            return name_list

        parameter_type, parameter_base = ask_for_parameters(name)
        name_list.append((name, parameter_type, parameter_base))

    return name_list
