from copy import deepcopy

from tournament_game.constants import LEADERBOARD_LENGTH
from tournament_game.dictionaries import HIGH_SCORES
from tournament_game.interactive import (
    ask_for_player_name,
    change_leaderboard_description,
)


# class for maintaining a table of records. It is activated immediately, but the user enters
# the table only when his money-box register reaches a value greater than the minimum position in
# the specified table (10th place) - HIGH_SCORES constant.
# класс для ведения таблицы рекордов. Активируется сразу, но пользователь входит в таблицу лишь
# когда его касса достигает значения больше, чем минимальная позиция в заданной
# таблице (10-е место) - константа HIGH_SCORES
class Standings:
    def __init__(self):
        self.name = None
        self.list_old = None
        self.position_old = None
        self.position_new = None
        self.leaderboard = {}
        leaderscores = deepcopy(HIGH_SCORES)
        leaders_list = sorted(leaderscores, key=leaderscores.get, reverse=True)
        for leader_index, leader_name in enumerate(leaders_list):
            self.leaderboard[leader_index + 1] = (
                leader_name,
                leaderscores[leader_name],
            )

    # Check if the table needs to be changed. Sorting in two cases:
    # 1. user did not enter the table before, but his money-box reached a value greater than
    # the minimum record from the table. The user is asked for a name and the high score table
    # is sorted. 2. the player is already in the table.
    # Проверка необходимости изменения таблицы. Сортировка в двух случаях:
    # 1. пользователь не входил ранее в таблицу, но его касса достигла значения больше,
    # чем минимальный рекорд из таблицы. У пользователя запрашивают имя и производится сортировка
    # таблицы рекордов. 2. игрок уже находится в таблице.
    def check_sort(self, cash: int):
        if self.name is None:
            scores_min = self.leaderboard[LEADERBOARD_LENGTH][1]
            if cash > scores_min:
                self.name = ask_for_player_name()
                self.leaderboard[LEADERBOARD_LENGTH + 1] = (self.name, cash)

        if self.name is not None:
            self.sort(cash)

    # sorting the leaderbord. Only the position of the user changes if his money-box exceeds
    # the number of funds of the player from the 10th place. Only 10 places are always displayed.
    # If the user's cash register matches the amount of money a player has from any place,
    # then if the place previously occupied by the user was lower than the place of this player,
    # the user takes a place one position lower. If the user's previous position was higher,
    # then the user ranks one position higher.
    # сортировка таблицы рекордов. Меняется только позиция пользователя, если его касса превышает
    # число средств игрока с 10-го месте. Выводится всегда только 10 мест. Если касса пользователя
    # совпадает с количеством денег у игрока с какого-либо места, то если ранее занимаемое
    # пользоватем место было ниже места данного игрока, пользователь занимает место на позицию ниже.
    # Если предыдущее место пользователя было выше, то пользователь занимает место на одну позицию
    # выше.
    def sort(self, cash: int):
        current_leaderboard = {}
        position_old = None
        for key in self.leaderboard:
            if self.leaderboard[key][0] == self.name:
                position_old = key
        if position_old:
            del self.leaderboard[position_old]
        position_new = None
        position_set = set(
            number
            for number in range(LEADERBOARD_LENGTH + 2)
            if number in self.leaderboard
        )
        iter_position_set = iter(position_set)
        start_position = 1
        next_leader_name, next_leader_cash = self.leaderboard[next(iter_position_set)]
        for position in range(start_position, LEADERBOARD_LENGTH + 2):
            if not position_new and (
                cash > next_leader_cash
                or (cash == next_leader_cash and position_old <= position)
            ):
                current_leaderboard[position] = (self.name, cash)
                position_new = position
            else:
                current_leaderboard[position] = (next_leader_name, next_leader_cash)
                try:
                    next_leader_name, next_leader_cash = self.leaderboard[
                        next(iter_position_set)
                    ]
                except StopIteration:
                    pass
        if not position_new:
            position_new = LEADERBOARD_LENGTH + 1
            current_leaderboard[position_new] = (self.name, cash)
        self.leaderboard = current_leaderboard
        change_leaderboard_description(self.leaderboard, position_old, position_new)
