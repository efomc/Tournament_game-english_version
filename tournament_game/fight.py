from itertools import combinations
from math import log10
from random import gauss
from typing import Dict, List, Tuple

from tournament_game.character import Character
from tournament_game.interactive import (
    print_strike_description,
    print_strike_result_description,
    print_strike_dice,
    print_fight_winner,
)
from tournament_game.constants import DICE_FIGHT_LIMIT


# Determination of the winner of the battle of two fighters. There are two instances
# of the Character class as input. There is only one winner at the end. The fight is modeled as
# a sequence of round (strike number strike_number). Each round is handled
# by the strike_model function. After each round, the armor value of each fighter is checked -
# the armor_curr attribute of the Character class. If a fighter's armor_curr is less than
# zero as a result of a round, they're out. When only one of the fighters remains, he,
# as an instance of the Character class, is passed out as the winner.
# Определение победителя боя двух бойцов. На входе два экземпляра класса Character.
# На выходе единственный - победитель. Бой моделируется как последовательность раундов
# (номер раунда strike_number). Каждый раунд обрабатывается функцией strike_model.
# После каждого раунда, проверяется значение брони каждого бойца -
# атрибут armor_curr класса Character. Если в результате раунда у бойца значение armor_curr
# меньше ноля, он выбывает. Когда остается только один из бойцов, он как экземпляр класса Character
# передается на выход в качестве победителя.
def fight_model(*fighters: Character) -> Character:
    fighters = list(fighters)
    for fighter in fighters:
        fighter.armor_curr = fighter.armor

    strike_number = 1
    while len(fighters) > 1:
        for fighter1, fighter2 in combinations(fighters, 2):
            strike_model(fighter1, fighter2, strike_number)

        fighters = [fighter for fighter in fighters if fighter.armor_curr >= 0]
        strike_number += 1

    winner = fighters.pop()
    print_fight_winner(winner.name)

    return winner


# Striking round simulation. There are two instances of the Character class as input.
# The function does not return data, but makes changes to the processed class instances.
# Actions: calculation of a random variable based on the normal probability distribution
# (gauss_dice). Determining on its basis whether a blow was struck and to whom (hit_model).
# If the blow is parried or both missed - return. If one of the opponents is hit,
# the Strike force is simulated (hit_strength_model) inflicted with this damage force (damage_model)
# and the reduction of the loser's armor by this damage (armor_crush_model).
# Моделирование раунда нанесения удара. На входе два экземпляра класса Character.
# Функция не возвращает данные, но вносит изменения в обрабатываемые экземпляры классов. Действия:
# вычисление случайной величины на основе нормального распределения вероятностей (gauss_dice).
# Определение на ее основе был ли нанесен удар и кому (hit_model).
# Если удар парирован или оба промахнулись - возврат.
# Если нанесен кому-то из противников, происходит моделирование силы удара (hit_strength_model),
# наносимого с этой силой урона (damage_model) и уменьшения брони проигравшего данным уроном
# (armor_crush_model).
def strike_model(fighter1: Character, fighter2: Character, strike_number: int):
    dice = gauss_dice(DICE_FIGHT_LIMIT)
    print_strike_dice(strike_number, dice)
    hit_result = hit_model(fighter1, fighter2, dice)
    if "strike" not in hit_result:
        print_strike_description(hit_result)
        return
    winner, loser = hit_result["strike"]
    print_strike_description(winner.name)
    hit_strength = round(hit_strength_model(winner), 1)
    damage = round(damage_model(hit_strength), 1)
    armor_crush_model(loser, damage)
    print_strike_result_description(damage, loser.name, loser.armor_curr)


# Checks if a hit was made.
# It takes two instances of the class (Character), the result of the throw (from 0 to 100,
# the throw limit is set by the variable DICE_FIGHT_LIMIT) and the number of the strike.
# Uses the Character attributes - name and duelling (from 0 to 100).
# A hit on the opponent is considered the case when the result of the roll is less than or
# equal to the duelling value of the fighter. To handle the result of a parry and a miss,
# the duelling of the first fighter is counted from 0 upwards, and the second fighter is counted
# from 100 downwards. In this case, the hit of the first fighter (hit_1) will be the case
# when dice is less than or equal to duelling, and the second (hit_2) is greater than
# or equal to 100 - duelling.
# If both miss (miss), the strike is parried (compensation), or the result is equal to the limit
# of their parameters (kiss), prints a message and returns nothing.
# If one of the fighters hits, returns a set of two instances of the Character class:
# the first position is the winner, the second is the loser.
# Проверяет, был ли нанесен удар.
# Принимает два экземпляра класса (Character), результат броска (от 0 до 100, предел броска задается
# переменной DICE_FIGHT_LIMIT) и номер удара.
# Использует атрибуты Character - name и duelling (от 0 до 100). Попадением по противнику считается
# случай, когда результат броска меньше или равен величине duelling бойца. Для обработки результата
# парирования и промаха, duelling первого бойца отсчитывается от 0 в сторону увеличения, а второго -
# от 100 в сторону уменьшения. В этом случае попаданием первого бойца (hit_1) будет случай, когда
# dice меньше или равно показателю duelling, а второго (hit_2) - больше или равно показателю
# 100 - duelling.
# Если оба промахнулись (miss), удар парирован (compensation), или результат равен границе их
# параметров (kiss), печатает сообщение и не возвращает ничего.
# Если кто-то из бойцов попадает, возвращает сет из двух экземпляров класса Character:
# на первой позиции победитель, на второй проигравший.
def hit_model(
    fighter1: Character, fighter2: Character, dice: int or float
) -> Dict[str, Tuple[Character, Character]] or str:
    fecht1 = fighter1.duelling
    fecht2 = fighter2.duelling

    hit_1 = fecht1 >= dice
    hit_2 = (DICE_FIGHT_LIMIT - fecht2) <= dice
    if hit_1 is not hit_2:
        winner = (fighter1, fighter2)[hit_2]
        loser = (fighter1, fighter2)[hit_1]
        hit_result = {"strike": (winner, loser)}
        return hit_result

    if fecht1 + fecht2 == DICE_FIGHT_LIMIT and dice == fecht1:
        hit_result = "kiss"
    elif hit_1 and hit_2:
        hit_result = "compensation"
    else:
        hit_result = "miss"
    return hit_result


# Calculates the hit strength as a random number from 0 to the value of the 'might' parameter
# using the gauss_dice function. The input is an instance of the Character class, the output
# is an integer - the value of the hit force.
# Вычисляет величину силы удара, как случайное число от 0 до величины параметра 'might' с помощью
# функции gauss_dice. На входе экземпляр класса Character, на выходе целое число -
# значение силы удара.
def hit_strength_model(fighter: Character) -> float:
    if isinstance(fighter.might, (int, float)) and fighter.might > 0:
        return gauss_dice(fighter.might)


# Calculates the amount of damage dealt. Takes the impact force as input.
# Returns the amount of damage dealt equal to the strength of the blow.
# Вычисляет величину наносимого урона. Принимает на входе силу удара.
# Возвращает величину наносимого урона, равную силе удара.
def damage_model(hit_strength: float or int) -> float or int:
    if isinstance(hit_strength, (int, float)) and hit_strength >= 0:
        hit_strength_result = hit_strength
    else:
        hit_strength_result = 0
    return hit_strength_result


# Reduces the armor value of the losing fighter, an instance of the Character class
# (current - armor_curr, initial equal to the 'armor' parameter)
# by the amount of damage to the armor (damage).
# Уменьшает значение брони проигравшего бойца, экземпляра класса Character (текущее - armor_curr,
# изначальное равно параметру 'armor') на величину повреждения брони (damage).
def armor_crush_model(loser: Character, damage: float or int) -> float or int:
    if isinstance(damage, (int, float)) and damage > 0:
        loser.armor_curr = round((loser.armor_curr - damage), 1)


# Returns a random integer from 0 to the value of the input parameter with a normal distribution:
# average value - half of the "parameter"
# 37% results with +-10% of average
# 66% from +-20% of average
# 77% from +-25% of average
# 95% c +-40% of average
# parameter must be an integer. But it will work with both float and negative ones.
# It makes no sense to pass numbers less than 10.
# Возвращает случайное целое число от 0 до значения передаваемого на входе параметра с
# нормальным распределением вероятности:
# среднее значение - половина параметра
# 37% результатов с +-10% от среднего
# 66% с +-20% от среднего
# 77% с +-25% от среднего
# 95% c +-40% от среднего
# parameter должен быть целым. Но сработает и с float, и отрицательными.
# Нет смысла передавать числа меньше 10.
def gauss_dice(parameter: int or float) -> int or float:
    if parameter != 0:
        round_base = int(log10(abs(parameter)))
    else:
        round_base = -2
    dice = 2 * gauss(parameter / 4, parameter / 9.09)
    if round_base <= 0:
        round_base = abs(round_base) + 2
        dice = float(round(dice, round_base))
    elif round_base <= 1:
        round_base = abs(round_base)
        dice = float(round(dice, round_base))
    else:
        round_base = 0
        dice = int(round(dice, round_base))
    correction = 1
    if parameter < 0:
        correction = -1
    if 0 <= correction * dice <= correction * parameter:
        return dice

    return gauss_dice(parameter)


# Returns the name of the character (class attribute Character.name),
# the first one in the list of fighters (all_fighters).
# The name is always a string
# Возвращает имя персонажа (атрибут класса Character.name), первого в списке бойцов (all_fighters)
# имя всегда строковое
def get_winner(all_fighters: List[Character]) -> str:
    return all_fighters[0].name
