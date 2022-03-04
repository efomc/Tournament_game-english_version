# Tournament_game, ver 1.0.eng


### authors: Egor Fomin in association with beresk_let

The Tournament_game simulates a tournament between different fighters, with the ability to choose fighters from different lists, create your own characters, bet on the outcome of fights or a tournament. The duel of each two fighters is based on the original combat model with a normal (Gaussian) probability distribution. The user interface provides easy localization into other languages.

# Bets

The main gameplay consists of bets. After creating (or generating a random) set of fighters, the user can place a bet on the winner of the tournament (the bet multiplier in case of MULTIPLIC_BET_TOURN_WINNER win depends on the number of participants), as well as place bets on the winner in each battle at all stages of the tournament.
If the user loses all cash, he is no longer asked for bets and is only consistently informed of the results of all the tournament's fights, up to the winner.

## Increasing difficulty:

The more cash the user has, the more difficult it is to place bets - the user receives less and less information about the fighters before the bet.
At the highest values of the player's money-box, information about fighters is not only reduced, but may also be unreliable (the percentage of unreliability is set by the UNRELIABLE_LIMIT constant). The intervals for changing the volume and reliability of the information supplied are specified in the CASH_STAGE_VALUES constant and are limited to 6 steps.

## Leaderboard

If the user increases the money-box more than the owner of the smallest record, he himself can get into the high score table and rise in it, from tournament to tournament, in order to eventually take first place.

# Selection and generation of tournament fighters:

When forming the list of tournament fighters, the user can set his own name for one, several or all fighters and one parameter for each (or not set parameters).
Also, the user can use ready-made sets of characters:
The user selects one or more of the ready-made sets, and the program randomly selects fighters from it for the tournament.
The user can create any number of his own fighters and choose from which sets the remaining ones will be recruited. The user can also not create their own fighters at all and use only ready-made kits.

## Formation of the list of fighters:

1. the user sets the total number of fighters from the given number of options (MULTIPLIC_BET_TOURN_WINNER),

2. the user chooses whether to create his own fighters - give them a name of their own choice. If the user specifies a name, then he can also specify one parameter. If it refuses to set a parameter, they are set to None and are randomly assigned during character creation. If the user refuses to set options, the user is prompted to set the name of the next fighter.

3. As soon as the user refuses to set a name, he is prompted to select sets of given names, from which the remaining fighters will be randomly selected up to a given number of participants.

At the output, we get a list from the character creation set: Name (name), given parameter (parameter_type), value category for the given parameter (parameter_base).

# Fight model (function fight_model):

To ensure the maximum speed of combat calculations, a simple and elegant model for calculating the results of fighters' strikes is the basis.
The model sequentially calculates the rounds (the strike_model function) in which both fighters can strike, and then handles its consequences for the fighters.
The result of each round can be a strike by one of the fighters, a mutual miss or a parry.
The only parameter responsible for the probability of hitting is ‘duelling’. 
The ‘might’ parameter is responsible for the force of striking, 
and the ‘armor’ parameter is responsible for the number of hits that the character can withstand.

## Striking

For each round, a single random number is generated (the result of the roll is ‘dice’) and mapped to each fighter's single parameter, dueling (the hit_model function).

A hit on the opponent is considered to be the case when the result of the roll is less than or equal to the duelling value of the fighter.

To ensure that the result of the round is determined by a single roll, the duelling of the first fighter is counted from 0 upwards, and the second - from 100 downwards. The hit of the first fighter (hit_1) is the case when dice is less than or equal to duelling, and the second (hit_2) is greater than or equal to 100 - duelling. If both parameters fall short of the dice value, both are missed. If both fighters hit, the blow is parried - (compensation).

If both miss (‘miss’), the strike is parried (‘compensation’), or the result is equal to the limit of their parameters (‘kiss’), prints a message and returns nothing.

Fighter 1 hit (‘duelling 1’ parameter):

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/t95V/gUMrmAXZs)

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/1VHJ/xfkzQQe6s)


Fighter 2 hit (‘duelling 2’ parameter):

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/C3qi/uKSBL3tTV)

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/6Vim/GTuNMuz6V)


compensation:

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/NhBX/u29mMVfsq)


miss:

![](https://thumb.cloud.mail.ru/weblink/thumb/xw1/QhrC/Cx4YBJoJg)


For ease of model management, the maximum value of the throw result and the duelling parameter are set to integers from 0 to 100 (the value of DICE_FIGHT_LIMIT, constants.py file), which allows it to be thought of as a "percentage".

## Normal distribution

For greater realism, the throw result is modeled with a normal (Gaussian) distribution (gauss_dice function). The mathematical expectation is 50 (half of DICE_FIGHT_LIMIT). Therefore, in the maximum number of cases, the value of the roll will be about 50. By analyzing a large number of samples, the variance is chosen in such a way that the distribution is fairly smooth:

37% results with +-10% around of half max roll value (DICE_FIGHT_LIMIT, i.e. 50)

66% с +-20% around 50

77% с +-25% around 50

95% c +-40% around 50


thus, low and high values still drop less frequently, which still leaves fighters with low ‘duelling’ values a chance to strike.

Throw values less than 0 and greater than the maximum value (in this case DICE_FIGHT_LIMIT) are cut off.

## Striking force

The force of hitting (function hit_strength_model) is modeled by a simple random number from 0 to the value of the fighter's strength (parameter might). For realism, i.e. to reproduce the situation that a person with a certain skill, as a rule, implements it, and does not miss or give an extraordinary result with equal probability, the impact force is also modeled by the same normal distribution (gauss_dice function) with the same scatter of results, only from half the size of might:

37% of results with +-10% around of half might

66% off +-20% around of half might

77% off +-25% around of half might

95% c +-40% around of half might


Thus, in the vast majority of cases, the magnitude of the impact will be half the value of might or will not differ much from it up or down.

If you wish, you can enter your own model for calculating the force of impact. For example, to introduce the influence of fatigue or the consequences of injuries, etc. If the result can be reduced to a single value "strength of impact", then only the hit_strength_model function will need to be changed, adding the appropriate attributes to the Character class, an instance of which is passed to the hit_strength_model function.

## Damage dealt (damage_model function)

In this release, the amount of damage is taken equal to the force of the hit.
If you wish, you can enter your own damage model. For example, introduce weapons for fighters with different parameters and defeat properties. If the result can be reduced to a single amount of damage (damage), then only the damage_model function needs to be changed.

## Armor crush (armor_crush_model function)

In this release, the amount of damage to armor is taken equal to the amount of damage (damage). The damage is simply subtracted from the current value of the armor value (armor_curr), which is equal to the “armor” parameter at the beginning of the battle and decreases with each missed hit.

You can optionally enter your own damage model. For example, enter different types of armor or a random value that affects the chance to reduce damage. If the result can be reduced to a single value of the armor value (armor), then only the armor_crush_model function will need to be changed.

# Balance (calibration)

## Creation of parameters of fighters:

To ensure a balance between fighters, only one of the parameters can have a ‘high’ score, one ‘normal’ and one ‘low’.

Also for balance, the magnitude categories of each parameter have different ranges of values. Corrections to value intervals are specified in the PARAMETERS_DELTAS constant. One amendment to each category of magnitude, increasing both the lower and upper limit of the category.

To create a character, you can specify at most one parameter in the form - parameter type (parameter_type from PARAMETERS_DELTAS) and value category (parameter_category from CATEGORIES_LIMITS). From the set of parameter types and categories, the specified values are excluded, the rest are distributed randomly.

If no parameters are given, the entire distribution is given randomly. Since different parameters affect the results of the battle in different ways, different corrections are used for the magnitude categories for different types of parameters (PARAMETERS_DELTAS).

## Calibration of parameter values:

To calibrate the game so that the outcome of combat is less predictable and characters with low ‘duelling’ but high ‘might’ or ‘armor’ can also win in a significant number of cases, the maximum value of ‘duelling’ is capped at 81.

At the same time, the ‘might’ and ‘armor’ parameters have been adjusted to increase both the minimum and maximum values in each parameter value category.

So, if the interval of values for ‘duelling’ in the ‘normal’ category is from 41 to 61, then the ‘normal’ interval for the ‘might’ parameter has a correction of 5 units and ranges from 46 to 67. And for the ‘armor’ parameter, a correction of 10 units and ranges from 51 to 61.

Value intervals and corrections are specified in the constants.py file by constants:

CATEGORIES_LIMITS - categories of magnitude

PARAMETERS_DELTAS - corrections for magnitude categories

## Result balance:

In the current release, a high ‘duelling’ parameter plays a decisive role in the victory of the character. If a fighter's ‘duelling’ parameter belongs to the high interval and is close to the maximum value, he will win with the maximum probability.

You can amend the model at your discretion (PARAMETERS_DELTAS constant)

# User interaction. Envisaged input errors

It is possible for the user to enter various answers to the program's questions (tuples ANSWER_OPTIONS_YES_NO_RUS_ENG, ENG_FIRST_FIGHTER_OPTIONS, ENG_SECOND_FIGHTER_OPTIONS), including entering characters in different registers. For example, for a request to enter "yes" or "no", the user can enter options for short or long answers, including those with an erroneous layout, from a tuple:

```
(
    "да",
    "1",
    "у",
    "lf",
    "fuf",
    "ага",
    "валяй",
    "конечно",
    "давай",
    "ладно",
    "хорошо",
    "yes",
    "ye",
    "y",
    "yeah",
    "yea",
    "yep",
    "yup",
)
```

Various responses are provided for user input of an unreadable response (tuples ENG_ERROR_OPTIONS_YES_NO and ENG_ERROR_MESSAGES_FOR_OPTIONS). After each erroneous input, the program responds with the next version of the error message. When the options run out, the last option is displayed each time.

You can add your own options for user responses and error messages.

# Simple localization

## Switching between built-in languages

At the moment, the program provides two languages of communication with the user - English and Russian. 

To switch the language, it is enough to change the only switch in the code - the dictionaries.py file, the choosen_language variable. Meaning “ENG” for English and “RUS” for Russian.

Without exception, the code takes all messages to the user from the dictionaries.py file. Localization requires changes only in this file.

## Simple localization into a new language:

The code provides easy localization to any new language. To do this, you need in the dictionaries.py file:

1. translate all dictionaries from the dictionary:

```
    "ENG": {
        "LOCALIZE_DICT": ENGLISH_LOCALIZE_DICT,
        "GENERAL_NAME_LIST": (
            ENG_NAME_LIST_HEROES,
            ENG_NAME_LIST_REAL,
            ENG_NAME_LIST_WALES,
        ),
        "HIGH_SCORES": ENGLISH_HIGH_SCORES,
        "ANSWER_OPTIONS_YES_NO": ANSWER_OPTIONS_YES_NO_RUS_ENG,
        "ERROR_OPTIONS_YES_NO": ENG_ERROR_OPTIONS_YES_NO,
        "ERROR_MESSAGES_FOR_OPTIONS": ENG_ERROR_MESSAGES_FOR_OPTIONS,
        "ROUND_NAMES": ENG_ROUND_NAMES,
        "FIRST_FIGHTER_OPTIONS": ENG_FIRST_FIGHTER_OPTIONS,
        "SECOND_FIGHTER_OPTIONS": ENG_SECOND_FIGHTER_OPTIONS,
        "STRIKE_RESULT_OPTIONS": ENG_STRIKE_RESULT_OPTIONS,
    },
```

2. specify the translated dictionaries in the new section of the dictionary by entering a new key (in this example, "Any new language") in string format, following the pattern:

```    
"Any new language": {
        "LOCALIZE_DICT": None,
        "GENERAL_NAME_LIST": (
            None,
        ),
        "HIGH_SCORES": None,
        "ANSWER_OPTIONS_YES_NO": None,
        "ERROR_OPTIONS_YES_NO": None,
        "ERROR_MESSAGES_FOR_OPTIONS": None,
        "ROUND_NAMES": None,
        "FIRST_FIGHTER_OPTIONS": None,
        "SECOND_FIGHTER_OPTIONS": None,
        "STRIKE_RESULT_OPTIONS": None,
    }
```

3. specify the value of the localization switch (your key for the DICT_VARIANT dictionary, in this example "Any new language") in the dictionaries.py file, the variable choosen_language in the format:

```
choosen\_language = "Any new language"
```

4. All dictionaries and messages necessary for the code to work will be automatically generated according to the choosen_language switch you specified as the key for the main localization dictionary DICT_VARIANT.

**IMPORTANT!**

The code generates the main message dictionary for the user (LOCALIZE_DICT) based on the keys of the ENGLISH_LOCALIZE_DICT dictionary. Therefore, when localizing, rely on this dictionary, and also carefully make sure that you have given the appropriate localization to all keys of the ENGLISH_LOCALIZE_DICT dictionary.

# Simple game extension

## Easily manage fighter sets

When forming a list of fighters, the user is offered a choice between sets from the DICT_VARIANT[choosen_language]["GENERAL_NAME_LIST"] tuple in the dictionaries.py file.

You can remove any of the name sets or add your own. The program will automatically prompt the user to choose between the sets that you leave.

## Add your fighters to existing sets or create your own set.

Lists of fighters of the tournament (if the user does not specify all the names himself) are formed randomly from sets selected by the user.

The list of sets the user is asked to choose from is in the tuple: DICT_VARIANT[choosen_language]["GENERAL_NAME_LIST"] of the dictionaries.py file.

Each set is a namedtuple of the structure: (str[list name], (character sets)).
The character set has the following structure:

(

index 0 - str[name],

index 1 - str[type of the given parameter (from the PARAMETERS_DELTAS set)],

index 2 - str[set parameter value category]

).

For each character, only one of the parameter types (parameter_type) and the value category of this parameter (parameter_base) are specified in string format. The exact values and the values of other parameters will be determined randomly. This provides some balance between characters of different properties.

To complete tuples with your own heroes, it is enough to either add the set/sets to the existing tuples (make sure that the tuple is included in the DICT_VARIANT[choosen_language]["GENERAL_NAME_LIST"] dictionary set of the given localization).

Name is a string value.

The type of the specified parameter is a string value strictly from among the options in the PARAMETERS_DELTAS dictionary.

The value category of the specified parameter is a string value strictly from among the options in the CATEGORIES_LIMITS dictionary.

You can also create your own named tuple with character sets.

Be sure to include this named tuple in the DICT_VARIANT[choosen_language]["GENERAL_NAME_LIST"] dictionaries set for this locale. Then when choosing character sets, the user will be prompted to select your new set. The program automatically offers the user a choice of sets from this tuple.


## Change the leaderboard

The starting highscore table is stored in the DICT_VARIANT[choosen_language][" HIGH_SCORES"] constant in the dictionaries.py file.

You can change the names in this table, or the value of the records, or the number of names in the table.

**IMPORTANT**: When printing, only the names with the highest scores are printed. The number of seats displayed to the user is determined by the LEADERBOARD_LENGTH constant in the constants.py file. If you change the number of names in the table, or the number of seats displayed to the user, make sure that LEADERBOARD_LENGTH is less than or equal to the number of seats in the original highscore table (HIGH_SCORES).


## Change the combat model of the game

You can make your own improvements to the battle process - change the models of impact force, damaging factors of weapons, damage to characters' armor. To do this, you just need to expand the existing individual functions in the fight.py file:

hit_strength_model

damage_model

armor_crush_model


# Project files:

**core.py** - main file. Contains the starting code for the game.

**fight.py** - fight model. All functions that handle combat between two characters (instances of the Character class).

**character.py** – the Character class (Character) and functions for creating a set of tournament fighters (all_fighters).

**moneybox.py** – the user's MoneyBox cash register class, and all transactions associated with it

**leaderboard.py** – the Standings leaderboard class and operations for adding a user to it and sorting

**interactive.py** - all functions responsible for interacting with the user - displaying messages to him, or asking him for data or solutions.

**perversion.py** - functions for giving incomplete reliability of information about characters passed to the user

**constants.py** – constants that set the parameters of the mathematical model of combat and game restrictions.

**dictionaries.py** - dictionaries and tuples with all, without exception, messages to the user. Also a set of dictionaries for localization (DICT_VARIANT) and a variable for switching the localization variant (choosen_language).

**tests** (directory) - contains tests. At the moment, the coverage is incomplete, the section is being finalized.

**IMPORTANT**: since the outcome of the battle and the creation of characters is probabilistic, a number of tests simulate a large number of creation cycles, or strikes or fights. Therefore, running a full suite of tests takes a long time and requires a significant amount of memory. It is recommended to run tests in separate packages.

**IMPORTANT**: at the moment, tests displaying information to the user are configured for the Russian version of localization.

# Requirements

Python 3.9+

Pytest 6.2.5+ for test package

setuptools 56+
