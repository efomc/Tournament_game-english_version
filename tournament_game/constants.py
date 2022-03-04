from collections import OrderedDict

# initial value limits for each parameter value category
# базовые пределы значений для каждой категории величины параметра
LOW_LIMITS = (30, 41)
NORMAL_LIMITS = (41, 61)
HIGH_LIMITS = (61, 81)

CATEGORIES_LIMITS = OrderedDict(
    {"low": LOW_LIMITS, "normal": NORMAL_LIMITS, "high": HIGH_LIMITS}
)

# corrections for the range of parameter values.
# For each category, an adjustment that increases the value in each
# of the three magnitude categories: low, normal, and high
# поправки для интервала значений параметров.
# Для каждой категории поправка, увеличивающая значение в каждой
# из трех категорий величины: low, normal и high
PARAMETERS_DELTAS = OrderedDict(
    {"duelling": (0, 0, 0), "might": (0, 5, 15), "armor": (0, 10, 20)}
)

# limit on the maximum value of a random variable in the battle model
# ограничение по максимальному значению случайной величины в модели боя
DICE_FIGHT_LIMIT = 100

# Coefficient of increase in winnings when betting on the winner of the tournament,
# depending on the number of participants in the tournament.
# коэффициент увеличения выигрыша при ставке на победителя турнира
# в зависимости от числа участников турнира
MULTIPLIC_BET_TOURN_WINNER = {
    4: 5,
    8: 10,
    16: 20,
    32: 30,
}

# number of steps in the leaderboard
# количество мест в таблице рекордов
LEADERBOARD_LENGTH = 10

# Measuring intervals of the cash register of users, in which fighters are described for users.
# Интервалы значений кассы пользователя, в которых описание бойцов для пользователя отличается.
CASH_STAGE_VALUES = {
    1: 150,
    2: 250,
    3: 400,
    4: 600,
    5: 1200,
}


# The probability of getting false information about a fighter. Integer in percent.
# Вероятность получить недостоверную информацию о бойце, целое число в процентах.
UNRELIABLE_LIMIT = 40


