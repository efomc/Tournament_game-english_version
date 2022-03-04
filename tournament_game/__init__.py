__version__ = "1.0.eng"

from .core import (  # noqa: F401
    main,
    tournament_round,
)

from .character import (
    Character,
    generate_characters,
    generate_name_list,
)

from .constants import (
    LOW_LIMITS,
    NORMAL_LIMITS,
    HIGH_LIMITS,
    CATEGORIES_LIMITS,
    PARAMETERS_DELTAS,
    DICE_FIGHT_LIMIT,
    MULTIPLIC_BET_TOURN_WINNER,
    LEADERBOARD_LENGTH,
    CASH_STAGE_VALUES,
    UNRELIABLE_LIMIT,
)

from .dictionaries import (
    LOCALIZE_DICT,
    GENERAL_NAME_LIST,
    HIGH_SCORES,
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

from .fight import (
    fight_model,
    strike_model,
    hit_strength_model,
    damage_model,
    armor_crush_model,
    hit_model,
    gauss_dice,
    get_winner,
)

from .interactive import (
    yes_no,
    choose_option,
    ask_for_fighters_number,
    ask_for_name,
    choose_name_list,
    ask_for_parameters,
    ask_for_bet_favorite,
    ask_bet_for_fight_winner,
    choose_for_favorite,
    choose_for_fight_winner,
    ask_bet_value,
    phrase_about_fighter,
    print_description_round_gain,
    print_pair_description,
    print_strike_description,
    print_strike_dice,
    print_strike_result_description,
    print_fight_winner,
    print_round_fighters_descriptions,
    print_tournament_winner,
    print_description_favorite_gain,
    print_description_tournament_gain,
    ask_for_player_name,
    change_leaderboard_description,
)

from .leaderboard import Standings

from .moneybox import MoneyBox

from .perversion import (
    get_extremum_parameter,
    get_worse_parameter,
    get_best_parameter,
)
