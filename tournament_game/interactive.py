from collections import OrderedDict
from random import shuffle
from typing import Tuple, Optional, Iterable, List

from tournament_game.constants import (
    PARAMETERS_DELTAS,
    CATEGORIES_LIMITS,
    LEADERBOARD_LENGTH,
    MULTIPLIC_BET_TOURN_WINNER,
    CASH_STAGE_VALUES,
)

from tournament_game.dictionaries import (
    LOCALIZE_DICT,
    GENERAL_NAME_LIST,
    ANSWER_OPTIONS_YES_NO,
    ERROR_OPTIONS_YES_NO,
    ERROR_MESSAGES_FOR_OPTIONS,
    ROUND_NAMES,
    FIRST_FIGHTER_OPTIONS,
    SECOND_FIGHTER_OPTIONS,
    STRIKE_RESULT_OPTIONS,
    WORSE_EPITHETS_DICT,
    BEST_EPITHETS_DICT,
)
from tournament_game.perversion import get_worse_parameter, get_best_parameter


# a function to receive a response from the user in the "yes"/"no" format. At the input,
# the string value question is the question that will be broadcast to the user,
# the response options from the user in the form of a tuple, which contains a tuple
# with "yes" answers and a tuple with "no" answers. By default, the ANSWER_OPTIONS_YES_NO constant
# is used and the options for reporting an error to the user about an input tuple error.
# The default is the ERROR_OPTIONS_YES_NO constant. If the user enters a response that is not
# in the response options, the next version of the error message is displayed to the user.
# When the messages are finished, it is displayed over and over again until the user enters
# an answer corresponding to any of the answer options. The output of the function is True or False.
# функция для получения от пользователя ответа в формате "да"/"нет". На входе строковое значение
# question - вопрос, который будет транслирован пользователю, варианты ответов от пользователя
# в виде кортежа, в который вложен кортеж с ответами "да" и кортеж с ответами "нет".
# По умолчанию используется константа ANSWER_OPTIONS_YES_NO и варианты сообщений пользователю об
# ошибке ввода кортеж. По умолчанию используется константа ERROR_OPTIONS_YES_NO. Если пользователь
# вводит ответ, которого нет в вариантах ответа, ему выводится следующий вариант сообщения
# об ошибке. Когда сообщения заканчиваются, выводится раз за разом последее, пока пользователь
# не введет ответ, соответствующий какому-либо из вариантов ответа. На выходе функция возвращает
# значение True или False.
def yes_no(
    question: str,
    answers: Tuple[Tuple[str], Tuple[str]] = ANSWER_OPTIONS_YES_NO,
    error_options: Tuple[str] = ERROR_OPTIONS_YES_NO,
) -> bool:
    positive_answers, negative_answers = answers
    error_messages = iter(error_options)
    error_message = None
    print(question)
    answer = input().lower()
    while answer not in (*positive_answers, *negative_answers):
        try:
            error_message = next(error_messages)
        except StopIteration:
            pass
        print(error_message)
        answer = input().lower()
    return answer in positive_answers


# The function of the user choosing one option from the proposed ones. At the input:
# question in string format - the question asked to the user;
# options_names is an iterable object with options (in string format) between which the user
# must choose.
# The function generates a description of options for the user to select by matching the options
# in the localization dictionary and asking the user to enter the selected option.
# If the user enters data that does not match any option, an error message is displayed from
# the ERROR_MESSAGES_FOR_OPTIONS constant. Each next time the next message is displayed.
# When they finish, the last message is displayed until the user gives an answer that matches
# one of the options. The output of the function is the name of the selected option from
# the options_names object.
# Функция выбора пользователем одного варианта из предложенных. На входе:
# question в строковом формате - задаваемый пользователю вопрос;
# options_names - итерируемый объект с вариантами (в строковом формате), между которыми пользователь
# должен выбрать. Функция формирует для пользователя описание вариантов для выбора, находя
# соответствие вариантам в словаре локализации и просит пользователя ввести выбранный вариант.
# Если пользователь вводит данные не соответствующие ни одному варианту, выводится сообщение
# об ошибке из константы ERROR_MESSAGES_FOR_OPTIONS. Каждый следующий раз выводится следующее
# сообщение. Когда они заканчиваются, выводится последнее сообщение, пока пользователь не даст
# ответ, соответствующий одному из вариантов. На выходе функция дает имя выбранного варианта из
# объекта options_names.
def choose_option(question: str, options_names: Iterable[str]) -> str:
    indexed_options = OrderedDict()
    indexed_options_localized = OrderedDict()
    for option_index, options_name in enumerate(options_names):
        index_key = option_index + 1
        localized_name = LOCALIZE_DICT[options_name]
        indexed_options[index_key] = options_name
        indexed_options_localized[index_key] = localized_name

    options_tuple = tuple(
        f"{index} - {value}" for index, value in indexed_options_localized.items()
    )
    options_string = "; ".join(options_tuple)
    question += f" \n[{options_string}]"

    error_messages = iter(ERROR_MESSAGES_FOR_OPTIONS)
    error_message = None

    answer = None
    while not answer:
        try:
            print(question)
            answer = int(input())
        except (TypeError, ValueError):
            pass

        if answer not in indexed_options_localized:
            try:
                error_message = next(error_messages)
            except StopIteration:
                pass
            print(error_message)
            answer = None

    return indexed_options[answer]


# The function of selecting the total number of fighters in the tournament by the user.
# Options for the number of fighters are suggested from the MULTIPLIC_BET_TOURN_WINNER dictionary.
# In case of an incorrect answer, an error message is displayed until the user selects
# one of the options for the number of fighters. At the output, the function passes an integer -
# the number of fighters in the tournament.
# Функция выбора пользователем общего числа бойцов турнира. Варианты числа бойцов предлагаются из
# словаря MULTIPLIC_BET_TOURN_WINNER. В случае неверного ответа выдается сообщение об ошибке,
# до тех пор, пока пользователь не выберет один из вариантов числа бойцов.
# На выходе функция передает целое число - число бойцов турнира.
def ask_for_fighters_number():
    tournament_level_list = sorted(list(set(MULTIPLIC_BET_TOURN_WINNER)))
    tournament_level_str_set = set(str(level) for level in tournament_level_list)
    tournament_level_str = ""
    for index, level in enumerate(tournament_level_list):
        if index == 0:
            tournament_level_str += str(level)
        elif index + 1 != len(tournament_level_list):
            tournament_level_str += f", {level}"
        else:
            tournament_level_str += f' {LOCALIZE_DICT["or"]} {level}'
    print(f'{LOCALIZE_DICT["number of fighters request"]}\n[{tournament_level_str}]')
    answer = input()
    while answer not in tournament_level_str_set:
        print(
            f"{LOCALIZE_DICT['incorrect! Only']} {tournament_level_str}, {LOCALIZE_DICT['please']}:"
        )
        answer = input()

    return int(answer)


# The function prompts the user to give their own name to the fighter.
# At the input, the number of the fighter (int), at the output, data of type bool
# Предложение пользователю дать собственное имя бойцу.
# На входе номер бойца (int), на выходе данные типа bool
def ask_for_name(fighter_index: int) -> Optional[str]:
    if fighter_index == 0:
        question = LOCALIZE_DICT["Shall we give name to the fighters?"]
    else:
        question = LOCALIZE_DICT["Will we give the next fighter a name?"]

    if yes_no(
        f'{question} ({LOCALIZE_DICT["If not, it will be set randomly"]})\n'
        f'[{LOCALIZE_DICT["yes/no"]}]'
    ):
        print(
            f"{LOCALIZE_DICT['What name will we give to fighter #']}{fighter_index + 1}?"
        )
        return input()


# The function of selecting a set of fighters by the user. The input is the number of fighters
# whose names and parameters need to be determined. The user is prompted to choose from which
# sets of names the list of fighters will be formed. The localized name sets are taken from
# the GENERAL_NAME_LIST tuple. From the names of named tuples with sets of characters,
# a description of the options for the user is automatically formed and a list of correct answers
# is formed. The user can select multiple sets by entering their numbers in any format,
# spaces and punctuation marks are ignored. Until the user enters at least one set number,
# he will receive an error message and be asked to repeat the entry. The sets of characters selected
# by the user are combined into one list, mixed randomly, and the required
# number of fighters (fighters_number) is selected from it. At the output,
# the function passes a list of sets for creating characters.
# Функция выбора пользователем набора бойцов. На входе передается число бойцов, имена и параметры
# которых требуется определить. Пользователю предлагается выбрать из каких наборов имен будет
# формироваться список бойцов. Локализованные наборы имен берутся из кортежа GENERAL_NAME_LIST.
# Из имен именованных кортежей с наборами персонажей автоматически формируется описание вариантов
# для пользователя и формируется список верных ответов. Пользователь может выбрать несколько
# наборов, введя их номера в любом формате, пробелы и знаки препинания игнорируются.
# Пока пользователь не введет номер хотя бы одного набора, ему будет выводиться сообщение об ошибке
# и просьба повторить ввод. Выбранные пользователем наборы персонажей объединяются в один список,
# перемешиваются случайным образом и от него отбирается необходимое число бойцов (fighters_number).
# На выходе функция передает список из наборов для создания перонажей.
def choose_name_list(fighters_number: int) -> List[Tuple[str, str, str]]:
    indexed_options_localized = enumerate(GENERAL_NAME_LIST)
    names_collecting_tuple = tuple(
        f"{index + 1} - {value.localized_description}"
        for index, value in indexed_options_localized
    )
    choise_set = set(f"{index + 1}" for index in range(len(GENERAL_NAME_LIST)))
    choise_options_list = list(
        f", {index + 1}" for index in range(len(GENERAL_NAME_LIST))
    )
    choise_options_list[-1] = choise_options_list[-1].replace(
        ", ", f' {LOCALIZE_DICT["or"]} '
    )
    choise_options_list[0] = choise_options_list[0].replace(", ", "")
    choise_options_str = "".join(choise_options_list)
    names_collecting_string = ", ".join(names_collecting_tuple)
    print(
        f"{LOCALIZE_DICT['what character sets will we use?']}:\n"
        f"[{names_collecting_string}\n"
        f"{LOCALIZE_DICT['spaces and punctuation are ignored']}]"
    )

    answer = input()
    correct_choices = choise_set.intersection(answer)
    while not correct_choices:
        print(
            f"{LOCALIZE_DICT['error message for choose name list']} {choise_options_str}"
        )
        answer = input()
        correct_choices = choise_set.intersection(answer)

    name_list = []
    for choice in correct_choices:
        extension_list = GENERAL_NAME_LIST[int(choice) - 1].characters_sets
        name_list.extend(extension_list)

    shuffle(name_list)

    return name_list[:fighters_number]


# The function of the user's choice of parameters for the fighter, whose name he set himself.
# At the input to the function, the name of the fighter, a string value.
# The output is a tuple of the parameter_name and parameter_category variables,
# which have either a string value from the PARAMETERS_DELTAS and CATEGORIES_LIMITS dictionaries,
# or the None value. The user is prompted to select options for the character they have named
# by calling the yes_no function. If the user agrees to set options, they are prompted to select
# only one of the options. The parameter names are selected from the localized dictionary
# for categories from the PARAMETERS_DELTAS dictionary by calling the choose_option function.
# After selecting the parameter type, the user is prompted to select the value category
# of this parameter also by calling the choose_option function. It is not possible to select only
# the type of parameter and not to select the category of the value of this parameter. If the user
# refuses to select options, they will be set to None and subsequently assigned randomly.
# Функция выбора пользователем параметров для бойца, чье имя он задал самостоятельно.
# На входе в функцию имя бойца, строковое значение. На выходе кортеж из переменных parameter_name и
# parameter_category, имеющих либо строковое значение из словарей PARAMETERS_DELTAS и
# CATEGORIES_LIMITS, либо значение None. Пользователю предлагается выбрать параметры для персонажа,
# имя для которого он задал, с помощью вызова функции yes_no. Если пользователь согласен задавать
# параметры, ему предлагается выбрать только один из параметров. Имена параметров выбираются из
# локализованного словаря для категорий из словаря PARAMETERS_DELTAS вызовом функции choose_option.
# После выбора типа параметра, пользователю предлагается выбрать категорию величины данного
# параметра также вызовом функции choose_option. Не предусмотрена возможность выбрать только тип
# параметра и не выбрать категорию величины данного параметра. Если пользователь откажется выбирать
# параметры, им будет присвоено значение None и впоследствии они будут назанчены случайным образом.
def ask_for_parameters(name: str) -> Tuple[Optional[str], Optional[str]]:
    parameter_name = None
    parameter_category = None

    if yes_no(
        f"{LOCALIZE_DICT['will we set parameters for this fighter?']}\n"
        f"[{LOCALIZE_DICT['yes/no']}]"
    ):
        question = f"{LOCALIZE_DICT['set parameter type for the fighter']} {name}?"
        parameter_name = choose_option(question, PARAMETERS_DELTAS)
        loc_parameter_name = LOCALIZE_DICT[parameter_name]
        question = (
            f'{LOCALIZE_DICT["set parameter category"]} "{loc_parameter_name}" '
            f'{LOCALIZE_DICT["for the fighter"]} {name}:'
        )
        parameter_category = choose_option(question, CATEGORIES_LIMITS)

    return parameter_name, parameter_category


# Asking the user whether they will bet on the winner of the tournament.
# The input contains a list of all fighters in the tournament (a list of all_fighters from instances
# of the Character class), the bet multiplication percentage in case of a win
# (index_for_tourn_winner, an integer) and the amount of funds on the user's hands (cash).
# Using the phrase_about_fighter function, the player is described all the fighters
# of the tournament and is asked to answer whether he will bet on the winner of the tournament.
# The choice is made by calling the yes_no function. At the output, the decision on the rate is
# in the form of a bool value.
# Запрос у пользователя, будет ли он делать ставку на победителя турнира. На входе список всех
# бойцов турнира (список all_fighters из экземпляров класса Character), процент умножения ставки
# в случае выигрыша (index_for_tourn_winner, целое число) и размер средств на руках
# пользователя (cash). С помощью функции phrase_about_fighter игроку описывают всех бойцов турнира и
# предлагается ответить, будет ли он делать ставку на победителя турнира. Выбор производится
# с помощью вызова функции yes_no. На выходе решение о ставке в виде значения типа bool.
def ask_for_bet_favorite(
    all_fighters: list, index_for_tourn_winner: int, cash: int
) -> bool:
    print(LOCALIZE_DICT["The following fighters compete at the tournament:"])
    # describe all the fighters of the tournament / описываем всех бойцов турнира:
    for index, fighter in enumerate(all_fighters):
        fighter_description = phrase_about_fighter(fighter, cash)
        print(f"{LOCALIZE_DICT['Fighter']} {index + 1}: {fighter_description}")

    # we bet on a single winner / делаем ставку на единственного победителя:
    return yes_no(
        f"{LOCALIZE_DICT['request for the winner of the tournament']} "
        f"{index_for_tourn_winner} {LOCALIZE_DICT['times']}"
    )


# Asks the user for the name of a fighter to bet on the winner of the tournament.
# The input is a list of fighters from instances of the Character class. From the list of fighters,
# it automatically generates and displays the list of fighters of the tournament to the user,
# prompts the user to select a player. The player can enter either the number of the fighter or
# his name. Other options are not accepted. Refusing to place a bet at this stage is not provided.
# The output is the selected fighter, an instance of the Charachter class.
# Запрашивает у пользователя имя бойца, для ставки на победителя турнира. На входе - список бойцов
# из экземпляров класса Character. Из списка бойцов автоматически формирует и выводит пользователю
# список бойцов турнира, запрашивает выбор игрока. Игрок может ввести либо номер бойца, либо его
# имя. Другие варианты не принимаются. Отказаться сделать ставку на этом этапе не предусмотрено.
# На выходе выбранный боец, экземпляр класса Charachter.
def choose_for_favorite(fighters: list):
    fighters_index = OrderedDict()
    fighters_catalogue = {}
    for index, fighter in enumerate(fighters):
        fighters_index[str(index + 1)] = fighter
        fighters_catalogue[fighter.name] = fighter

    print(LOCALIZE_DICT["request for name for bet"])
    for index, fighter in fighters_index.items():
        print(f"{index} - {fighter.name}")

    while True:
        answer = input()

        if answer in fighters_index:
            return fighters_index[answer]

        if answer in fighters_catalogue:
            return fighters_catalogue[answer]

        print(LOCALIZE_DICT["error options choose fighter for bet"])


# Asking the user whether he will bet on the winner of one fight. Using the yes_no function,
# the user is prompted to answer whether he will bet on the winner of the battle. At the output,
# the decision on the rate is in the form of a bool value.
# Запрос у пользователя, будет ли он делать ставку на победителя одного боя. С помощью функции
# yes_no пользователю предлагается ответить, будет ли он делать ставку на победителя боя. На выходе
# решение о ставке в виде значения типа bool.
def ask_bet_for_fight_winner() -> bool:
    return yes_no(
        f"{LOCALIZE_DICT['request for bet for the winner of the fight']}\n"
        f"[{LOCALIZE_DICT['If he wins the fight, the bet will increase by']} 2 "
        f"{LOCALIZE_DICT['timess']}. {LOCALIZE_DICT['answer options']}: {LOCALIZE_DICT['yes/no']}]"
    )


# Gets the user's answer on which of the two participants in the fight he bets. At the input,
# the tuple has two participants. The player can enter either the number of a fighter
# (in various forms defined by the FIRST_FIGHTER_OPTIONS and SECOND_FIGHTER_OPTIONS tuples),
# or his name. Other options are not accepted. It is not possible to refuse to make a bet
# at this stage. The response is received using the yes_no function. The output is a choice in
# the bool data format: False for fighter 1 and True for fighter 2.
# Получает ответ пользователя, на кого из двух участников боя он ставит. На входе - кортеж имет двух
# участников. Игрок может ввести либо номер бойца (в разных формах, определенных кортежами
# FIRST_FIGHTER_OPTIONS и SECOND_FIGHTER_OPTIONS, либо его имя. Другие варианты не принимаются.
# Отказаться сделать ставку на этом этапе не предусмотрено. Получение ответа производится с помощью
# функции yes_no. На выходе выбор в формате данных bool: False для бойца 1 и True для бойца 2.
def choose_for_fight_winner(fighters_names_tuple: tuple) -> bool:
    first_fighter_name, second_fighter_name = fighters_names_tuple

    first_fighter_options = FIRST_FIGHTER_OPTIONS + (first_fighter_name.lower(),)

    second_fighter_options = SECOND_FIGHTER_OPTIONS + (second_fighter_name.lower(),)

    answers_fighters = (first_fighter_options, second_fighter_options)

    question = (
        f"{LOCALIZE_DICT['request for name for bet']}\n"
        f"[1 - {first_fighter_name}. 2 - {second_fighter_name}]"
    )

    return not yes_no(
        question,
        answers_fighters,
        LOCALIZE_DICT["error options choose fighter for bet"],
    )


# Asks the user for the amount to bet. The input is the name of the fighter, the size of
# the user's money-box and the multiplier of the bet in case of a win (optional; default is 2).
# Requests how much the user is willing to wager from available funds. Accepts a bet
# if it is less than or equal to the user's money-box. Displays a message about the accepted bet.
# Returns the rate value in int format.
# Запрашивает у пользователя величину ставки. На входе имя бойца, размер кассы пользователя и
# коэффициент умножения ставки в случае выигрыша (не обязателен; по умолчанию 2). Запрашивает,
# сколько пользователь готов поставить из имеющихся средств. Принимает ставку, если она меньше или
# равна кассе пользователя. Выводит сообщение о принятой ставке.
# Возвращает значение ставки в формате int.
def ask_bet_value(
    fighter_name: str, cash: int, index_for_winner: Optional[int] = 2
) -> int:
    print(
        f"{LOCALIZE_DICT['bet value request']} \n"
        f"[{LOCALIZE_DICT['you have at your disposal']}: {cash}]"
    )

    while True:
        answer = input()
        try:
            answer = int(answer)
        except (TypeError, ValueError):
            print(LOCALIZE_DICT["error options for choose bet value with input type"])
            continue

        if answer <= 0:
            print(
                LOCALIZE_DICT["error options for choose bet value with input interval"]
            )
            continue
        elif answer <= cash:
            print(
                f"{LOCALIZE_DICT['Bets accepted!']} "
                f"{answer} {LOCALIZE_DICT['for fighter']} {fighter_name}.\n"
                f"{LOCALIZE_DICT['left in your moneybox']}: {cash - answer}\n"
                f"{LOCALIZE_DICT['If he wins, you win']} {answer * index_for_winner}"
            )
            return answer

        print(LOCALIZE_DICT["error options for choose bet value with money-box size"])


# Generates a description of the fighter. At the input is a fighter, as an instance of
# the Character class and the size of the player's cash register. The description depends on
# the size of the cash register - the larger the cash register, the shorter the description and
# the less reliable it is (implemented using the get_worse_parameter and get_best_parameter
# functions. The output is a description of the fighter in str format.
# Формирует описание бойца. На входе боец, как экземпляр класса Character и размер кассы игрока.
# Описание зависит от размера кассы - чем больше касса, тем короче описание и тем менее оно
# достоверно (реализуется с помощью функций get_worse_parameter и get_best_parameter.
# На выходе - описание бойца в формате str.
def phrase_about_fighter(fighter, cash: int):
    localize_best_par = LOCALIZE_DICT[fighter.best_parameter]
    localize_worse_par = LOCALIZE_DICT[fighter.worse_parameter]
    if cash < CASH_STAGE_VALUES[1]:
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['duelling'].capitalize()} - {fighter.duelling}, "
            f"{LOCALIZE_DICT['might']} - {fighter.might}, "
            f"{LOCALIZE_DICT['armor']} - {fighter.armor}."
        )
    elif cash < CASH_STAGE_VALUES[2]:
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['best parameter'].capitalize()}: "
            f"{localize_best_par} - "
            f"{fighter.parameters[fighter.best_parameter]}, "
            f"{LOCALIZE_DICT['but worst']}: {localize_worse_par} - "
            f"{fighter.parameters[fighter.worse_parameter]}."
        )
    elif cash < CASH_STAGE_VALUES[3]:
        worse_parameter = get_worse_parameter(
            fighter.parameters, fighter.best_parameter, fighter.worse_parameter
        )
        worse_epithet = WORSE_EPITHETS_DICT[worse_parameter]
        local_worse_epith = LOCALIZE_DICT[worse_epithet]
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['best parameter'].capitalize()}: "
            f"{localize_best_par} - "
            f"{fighter.parameters[fighter.best_parameter]}, "
            f'{LOCALIZE_DICT["but he probably"]}, {local_worse_epith}'
        )
    elif cash < CASH_STAGE_VALUES[4]:
        worse_parameter = get_worse_parameter(
            fighter.parameters, fighter.best_parameter, fighter.worse_parameter
        )
        best_epithet = BEST_EPITHETS_DICT[fighter.best_parameter]
        worse_epithet = WORSE_EPITHETS_DICT[worse_parameter]
        local_best_epith = LOCALIZE_DICT[best_epithet]
        local_worse_epith = LOCALIZE_DICT[worse_epithet]
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['very'].capitalize()} {local_best_epith} "
            f"{LOCALIZE_DICT['and']}, {LOCALIZE_DICT['probably']}, {local_worse_epith}"
        )
    elif cash < CASH_STAGE_VALUES[5]:
        best_epithet = BEST_EPITHETS_DICT[fighter.best_parameter]
        local_best_epith = LOCALIZE_DICT[best_epithet]
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['very'].capitalize()} {local_best_epith}."
        )
    else:
        best_parameter = get_best_parameter(fighter.parameters, fighter.best_parameter)
        best_epithet = BEST_EPITHETS_DICT[best_parameter]
        local_best_epith = LOCALIZE_DICT[best_epithet]
        fighter_about = (
            f"{fighter.name}. {LOCALIZE_DICT['probably'].capitalize()}, "
            f"{LOCALIZE_DICT['very']} {local_best_epith}."
        )
    return fighter_about


# Displays to the user a description of the win or loss from a localized dictionary.
# At the input, the size of the money-box (final) and the size of the winnings
# (optional; by default - None).
# Выводит пользователю описание выигрыша или проигрыша из локализованного словаря. На входе размер
# кассы (итоговый) и размер выигрыша (не обязательный; по умолчанию - None).
def print_description_round_gain(cash: int, gain: Optional[str] = None):
    if gain:
        print(LOCALIZE_DICT["You guessed the winner!"])
        print(
            f"{LOCALIZE_DICT['The gainings amounted to']}: {gain}. "
            f"{LOCALIZE_DICT['At the moneybox now']} {cash}"
        )
    else:
        print(
            f"{LOCALIZE_DICT['Eah']}! {LOCALIZE_DICT['The bet did not work']}. "
            f"{LOCALIZE_DICT['left in your moneybox']}: {cash}"
        )


# Displays to the user a description of the fighters using a localized dictionary. At the input,
# an iterable object from instances of the Character class, the number of the battle,
# the number of battles of this tournament stage, the size of the user's money-box
# (the description of the character depends on it). To form a phrase describing a fighter,
# the phrase_about_fighter function is used.
# Выводит пользователю описание бойцов с помощью локализованного словаря. На входе итерируемый
# объект из экземпляров класса Character, номер боя, число боев данного турнирного этапа,
# размер кассы пользователя (от него зависит описание персонажа).
# Для формирования фразы, описывающей бойца, используется функция phrase_about_fighter.
def print_pair_description(
    fighters: Iterable, fight_index: int, number_fights: int, cash: int
):
    if number_fights > 1:
        print(f"\n{LOCALIZE_DICT['fight'].capitalize()} №{fight_index + 1}")
    print(f"{LOCALIZE_DICT['participants'].capitalize()}: ")
    index = 0
    for fighter in fighters:
        index += 1
        fighter_about = phrase_about_fighter(fighter, cash)
        print(f"{LOCALIZE_DICT['Fighter']} {index}: {fighter_about}")


# Displays a message about a fighter hitting.
# Выводит сообщение о нанесении бойцом удара.
def print_strike_description(
    hit_result: str,
):

    if hit_result in STRIKE_RESULT_OPTIONS:
        print(STRIKE_RESULT_OPTIONS[hit_result])
    else:
        print(f"{LOCALIZE_DICT['successful was strike by']} {hit_result}.")


# Displays a message about the size of the random variable that determines the hit (dice).
# Выводит сообщение о размере случайной величины, определяющей удар (бросок/dice).
def print_strike_dice(
    strike_number: int,
    dice: float,
):
    print(
        f"\n{LOCALIZE_DICT['Strike by']} {strike_number}\n{LOCALIZE_DICT['Dice is']} {dice}"
    )


# Describes the force of the hit, the damage dealt, and the total armor value of the fighter
# who was hit.
# Описывает силу удара, нанесенный урон и итоговое значение брони бойца, которому нанесели удар.
def print_strike_result_description(
    damage: float, loser_name: str, loser_armor_curr: int
):
    print(
        f"{LOCALIZE_DICT['He did damage equal to']} {damage}.\n"
        f"{LOCALIZE_DICT['Armor of']} {loser_name} "
        f"{LOCALIZE_DICT['is now equal to']} {loser_armor_curr}"
    )


# Displays a message about the winner of the fight.
# Выводит сообщение о победителе боя.
def print_fight_winner(winner_name: str):
    print(f"{LOCALIZE_DICT['the winner is'].capitalize()} {winner_name}!\n")


# Displays the description of the fighters of the tournament stage. For all stages except the final.
# Выводит описание бойцов турнирного этапа. Для всех этапов, кроме финала.
def print_round_fighters_descriptions(fighters_pairs: tuple):
    round_name = ROUND_NAMES[len(fighters_pairs) * 2]
    print(f"\n{round_name}")
    if len(fighters_pairs) != 1:
        print(f"{LOCALIZE_DICT['competitors'].capitalize()}:")
        for fight_index, fighters in enumerate(fighters_pairs):
            first_fighter, second_fighter = fighters
            print(f"{LOCALIZE_DICT['fight'].capitalize()} {fight_index + 1}: "
                  f"{LOCALIZE_DICT['Fighter'].lower()} {first_fighter.name} "
                  f"{LOCALIZE_DICT['versus']} {LOCALIZE_DICT['versus fighter']} "
                  f"{second_fighter.name}")


# Displays a message about the winner of the tournament.
# Выводит сообщение о победителе турнира.
def print_tournament_winner(winners_name: str):
    print(f"{winners_name} {LOCALIZE_DICT['won the tournament']}!")


# Displays the result of a bet on the winner of the tournament.
# Выводит результат ставки на победителя турнира.
def print_description_favorite_gain(cash, favorites_name, gain: Optional[int] = None):
    if gain:
        print(
            f"{LOCALIZE_DICT['You guessed the winner of the tournament!']} "
            f"{LOCALIZE_DICT['The gain is']} {gain}. "
            f"{LOCALIZE_DICT['Total in the moneybox']}: {cash}"
        )
    else:
        print(
            f"{LOCALIZE_DICT['Your bet was on the fighter']} {favorites_name}. "
            f"{LOCALIZE_DICT['The bet did not work']}."
        )


# Describes the change in the user's cashier as a result of the entire tournament -
# the total win or loss, the total amount of funds.
# Описывает изменение кассы пользователя в результате всего турнира -
# общий выигрыш или проигрыш, итоговое количество средств.
def print_description_tournament_gain(gain: int, cash: int, record_high: int):
    if gain == 0:
        print(LOCALIZE_DICT["You didn't win anything for the tournament."])
    elif gain > 0:
        print(f"{LOCALIZE_DICT['Your winnings for the tournament']} {gain}.")
    else:
        print(f"{LOCALIZE_DICT['Your tournament loss']} {-gain}.")

    if cash > record_high:
        print(
            f"{LOCALIZE_DICT['As a result of the tournament, the moneybox reached']} {cash}. "
            f"{LOCALIZE_DICT['And this is a new record high!']}"
        )
    else:
        print(f"{LOCALIZE_DICT['The final checkout']}: {cash}")


# Reports when a user is in the leaderboard table and asks for a username.
# Accepts any response, even empty input. Returns in string format.
# Сообщает о попадании пользователя в таблицу рекордов и запрашивает имя пользователя.
# Принимает любой ответ, даже пустой ввод. Возвращает в строковом формате.
def ask_for_player_name() -> str:
    return input(LOCALIZE_DICT["You are on the leaderboard! Enter your name:"] + " ")


# Describes the changes in the user's position in the leaderboard
# based on the result of the tournament.
# Описывает изменения позиции пользователя в таблице рекордов по результату турнира.
def change_leaderboard_description(
    leaderboard: dict,
    position_old: int,
    position_new: int,
):
    if position_old == position_new >= LEADERBOARD_LENGTH + 1:
        pass
    else:
        if position_old != position_new >= LEADERBOARD_LENGTH + 1:
            print(LOCALIZE_DICT["You are out of the leaderboard"])
        elif position_old > position_new:
            print(
                f"{LOCALIZE_DICT['You have moved up to']} "
                f"{position_new}{LOCALIZE_DICT['th place']}."
            )
        elif position_old < position_new:
            print(
                f"{LOCALIZE_DICT['You have moved down to']} "
                f"{position_new}{LOCALIZE_DICT['th place']}."
            )
        else:
            print(
                LOCALIZE_DICT["You have remained in the same place in the leaderboard."]
            )

        for index in range(LEADERBOARD_LENGTH):
            leader_name, leader_cash = leaderboard[index + 1]
            print(f"{index + 1}\t{leader_name.ljust(20)}\t{leader_cash}")
