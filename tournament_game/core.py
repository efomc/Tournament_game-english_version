from typing import List

from tournament_game.dictionaries import LOCALIZE_DICT
from tournament_game.leaderboard import Standings
from tournament_game.moneybox import MoneyBox
from tournament_game.fight import get_winner, fight_model
from tournament_game.character import Character, generate_characters
from tournament_game.interactive import (
    yes_no,
    print_round_fighters_descriptions,
    print_tournament_winner,
    print_pair_description,
)


# Single round tournament. We get an instance of the moneybox class -
# the player's cash desk with bets and their results, and a list of fighters.
# The elements of the list of fighters are instances of the Character class.
# We give a description of the fighters, divide the fighters into pairs.
# Before each fight, we accept bets on the outcome of the fight. We fight between couples.
# If a bet was made on the winner, we process the result of the bet.
# Based on the results of each fight, the winner is included in the list for the next round
# of the tournament. The function returns a list of the winners of the given round.
# The elements of the list are instances of the Character class.
# Единичный раунд турнира. Получаем экземпляр класса moneybox - касса игрока со ставками и
# их результатом и список бойцов. Элементы списка бойцов - экземпляры класса Character.
# Даем описание бойцов, разбиваем бойцов на пары. Перед каждым боем принимаем ставки на исход боя.
# Проводим бои между парами. Если была сделана ставка на победителя, обрабатываем результат ставки.
# По итогам каждого боя победитель включается в список на следующий раунд турнира.
# Функция возвращает список бойцов-победителей данного раунда.
# Элементы списка - экземпляры класса Character.
def tournament_round(money_box: MoneyBox, fighters: List[Character]) -> List[Character]:
    fighters_pairs = tuple(zip(fighters[::2], fighters[1::2]))
    print_round_fighters_descriptions(fighters_pairs)

    winners = []
    for fight_index, fighters in enumerate(fighters_pairs):
        print_pair_description(
            fighters, fight_index, len(fighters_pairs), money_box.cash_end_balance
        )
        money_box.bet_round_winner(fighters)
        winner = fight_model(*fighters)

        if money_box.current_bet_fighter is not None:
            money_box.gain_round_winner(winner)

        winners.append(winner)

    return winners


# Start code. We create the player's money-box as an instance of the MoneyBox class,
# a leaderboard (standings, an instance of the Standings class).
# As long as the player agrees to continue playing, we conduct tournament cycles.
# We create a list of fighters, we offer to bet on the winner of the tournament.
# We play fights - until one fighter remains as a result of the round,
# we carry out tournament rounds. We display a message about the winner of the tournament.
# If a bet was made on the winner of the tournament, we process the result of the bet.
# We calculate and describe changes in the user's money-box (money_box.game_set_end function).
# Change the player's place in the high scores table if the money-box size allows it
# (function: standings.check_sort). Finally, we ask the user for consent to hold a new tournament.
# Пусковой код. Создаем кассу игрока как экземпляр класса MoneyBox, таблицу рекордов
# (standings, экземпляр класса Standings). Пока игрок согласен продолжать играть,
# проводим циклы турниров. Создаем список бойцов, предлагаем сделать ставку на победителя турнира.
# Проводим бои - пока в результате раунда не останется один боец, проводим раунды турнира.
# Выводим сообщение о победителе турнира. Если была сделана ставка на победителя турнира,
# обрабатываем результат ставки. Вычисляем и описываем изменения кассы пользователя
# (функция money_box.game_set_end). Изменяем место игрока в таблице рекордов, если размер кассы
# позволяет это (функция: standings.check_sort).
# Запрашиваем у пользователя согласие на проведение нового турнира.
def main():
    money_box = MoneyBox()
    standings = Standings()
    print(LOCALIZE_DICT["greeting message"])

    answer = True
    while answer:
        all_fighters = generate_characters()

        # Changing money_box state
        money_box.bet_tourn_winner(all_fighters)

        while len(all_fighters) > 1:
            all_fighters = tournament_round(money_box, all_fighters)

        winners_name = get_winner(all_fighters)
        print_tournament_winner(winners_name)

        # Changing money_box and standings state
        money_box.game_set_end(winners_name)
        standings.check_sort(money_box.cash_start_balance)

        answer = yes_no(LOCALIZE_DICT["continue message"])

    yes_no(LOCALIZE_DICT["close window request"])


if __name__ == "__main__":
    main()
