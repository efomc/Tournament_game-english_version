from operator import attrgetter
from typing import Tuple

from tournament_game.constants import MULTIPLIC_BET_TOURN_WINNER
from tournament_game.interactive import (
    ask_for_bet_favorite,
    ask_bet_for_fight_winner,
    ask_bet_value,
    print_description_round_gain,
    print_description_favorite_gain,
    print_description_tournament_gain,
    choose_for_favorite,
    choose_for_fight_winner,
)
from tournament_game.character import Character


# The user's money-box and all operations associated with it.
# Касса пользователя и все операции, с нею связанные.
class MoneyBox:
    def __init__(self):
        self.name = None
        self.cash_start_balance = 100
        self.cash_end_balance = self.cash_start_balance
        self.current_bet_value = None
        self.current_bet_fighter = None
        self.index_for_tourn_winner = None
        self.winner_bet_value = None
        self.winner_bet_fighter = None
        self.record_high = self.cash_start_balance

    # request and accept a bet on the winner of the tournament
    # запрашиваем и принимаем ставку на победителя турнира
    def bet_tourn_winner(self, all_fighters):
        bet_for_tourn_winner = False
        self.index_for_tourn_winner = MULTIPLIC_BET_TOURN_WINNER[len(all_fighters)]
        if self.cash_end_balance > 0:
            bet_for_tourn_winner = ask_for_bet_favorite(
                all_fighters,
                self.index_for_tourn_winner,
                self.cash_end_balance,
            )
        if bet_for_tourn_winner:
            choosen_tourn_winner = choose_for_favorite(all_fighters)
            self.winner_bet_fighter = choosen_tourn_winner.name
            bet = ask_bet_value(
                self.winner_bet_fighter,
                self.cash_end_balance,
                self.index_for_tourn_winner,
            )
            self.cash_end_balance -= bet
            self.winner_bet_value = bet

    # request and accept a bet on the winner of one fight
    # запрашиваем и принимаем ставку на победителя одного боя
    def bet_round_winner(
        self,
        fighters: Tuple[Character, Character],
    ):
        if self.cash_end_balance <= 0:
            return

        if not ask_bet_for_fight_winner():
            return

        fighters_names_tuple = tuple(map(attrgetter("name"), fighters))
        bet_fighter_index = choose_for_fight_winner(fighters_names_tuple)
        self.current_bet_fighter = fighters[bet_fighter_index].name

        bet_value = ask_bet_value(self.current_bet_fighter, self.cash_end_balance)
        self.cash_end_balance -= bet_value
        self.current_bet_value = bet_value

    # check the winnings as a result of the fight and replenish or reduce the user's money-box
    # проверяем выигрыш в результате боя и пополняем или уменьшаем кассу пользователя
    def gain_round_winner(self, winner: Character):
        if winner.name == self.current_bet_fighter:
            gain = self.current_bet_value * 2
            self.cash_end_balance += gain
        else:
            gain = None
        self.current_bet_value = 0
        self.current_bet_fighter = None
        print_description_round_gain(self.cash_end_balance, gain)

    # check the winning or losing bet on the winner of the tournament and replenish or
    # reduce the user's money-box
    # проверяем выигрыш или проигрыш ставки на победителя турнира и пополняем или уменьшаем
    # кассу пользователя
    def count_tourn_winner(self, winners_name: str):
        if winners_name == self.winner_bet_fighter:
            set_gain = self.winner_bet_value * self.index_for_tourn_winner
            self.cash_end_balance += set_gain
        else:
            set_gain = None
        print_description_favorite_gain(
            self.cash_end_balance, favorites_name=self.winner_bet_fighter, gain=set_gain
        )
        self.winner_bet_value = 0
        self.winner_bet_fighter = None

    # calculate the changes in the user's money-box as a result of the tournament
    # and display the results to the user
    # вычисляем изменения кассы пользователя в результате турнира и отображаем пользователю итоги
    def game_set_end(self, winners_name: str):
        if self.winner_bet_fighter is not None:
            self.count_tourn_winner(winners_name)
        gain = self.cash_end_balance - self.cash_start_balance
        print_description_tournament_gain(gain, self.cash_end_balance, self.record_high)

        if self.cash_end_balance > self.record_high:
            self.record_high = self.cash_end_balance
        self.cash_start_balance = self.cash_end_balance
