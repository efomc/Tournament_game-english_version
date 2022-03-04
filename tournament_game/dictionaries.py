from collections import namedtuple

# The main message dictionary for the user. When localization,
# it is recommended to use it as a basis, since localization dictionaries are filled
# on the basis of this dictionary.
# Основной словарь сообщений для пользователя. При переводе рекомендуется использовать именно
# его для основы, поскольку словари локализации наполняются на основе этого словаря.
ENGLISH_LOCALIZE_DICT = {
    "greeting message": "Welcome to the tournament game!",
    "continue message": "Shall we continue the game with another tournament?",
    "close window request": 'To close the game window, enter "yes" or "no"',
    "number of fighters request": "How many fighters will fight?",
    "incorrect! Only": "You enter inappropriately. Only",
    "please": "please",
    "Shall we give name to the fighters?": "Shall we give name to the fighters?",
    "Will we give the next fighter a name?": "Will we give the next fighter a name?",
    "If not, it will be set randomly": "If not, it will be set randomly",
    "yes/no": "yes/no",
    "What name will we give to fighter #": "What name will we give to fighter #",
    "or": "or",
    "what character sets will we use?":
        "What character sets will we use? You can select multiple sets from the following:",
    "spaces and punctuation are ignored": "spaces and punctuation are ignored",
    "error message for choose name list": "Input not recognized. Only numbers from:",
    "will we set parameters for this fighter?":
        "Will we set parameters for this fighter? (If not, they will be randomly assigned)",
    "set parameter type for the fighter": "What type of parameter do we set for the fighter",
    "set parameter category": "How high will the parameter value be?",
    "for the fighter": "for the fighter",
    "The following fighters compete at the tournament:":
        "The following fighters compete at the tournament:",
    "Fighter": "Fighter",
    "versus fighter": "fighter",
    "request for the winner of the tournament":
        "Let's bet right now on the winner of the tournament? \n"
    "If he wins everyone, the bet will increase by",
    "times": "times",
    "timess": "times",
    "request for bet for the winner of the fight": "Shall we bet on one of them?",
    "If he wins the fight, the bet will increase by":
        "If he wins the fight, the bet will increase by",
    "answer options": "Answer options",
    "request for name for bet": "Which fighter will we bet on?",
    "error options choose fighter for bet":
        "You enter inappropriately. Only the number or name of the fighter, please:",
    "bet value request": "How much do we bet?",
    "you have at your disposal": "you have at your disposal",
    "error options for choose bet value with input type":
        "Enter an integer. Only an integer, only a number!",
    "error options for choose bet value with input interval":
        "The bet must be greater than zero, of course!",
    "error options for choose bet value with money-box size":
        "You don't have that much money. Bet less!",
    "Bets accepted!": "Bets accepted!",
    "left in your moneybox": "What's left in your moneybox",
    "for fighter": "for the fighter",
    "If he wins, you win": "If he wins, you win",
    "best parameter": "best parameter",
    "but worst": "but worst",
    "but he probably": "but he's probably",
    "very": "very",
    "and": "and",
    "probably": "probably",
    "duelling": "duelling",
    "might": "might",
    "armor": "armor",
    "low": "low",
    "normal": "normal",
    "high": "high",
    "dexterous": "dexterous",
    "strong": "strong",
    "steel-clad": "steel-clad",
    "unskillful": "unskillful",
    "weak": "weak",
    "exposed": "exposed",
    "You guessed the winner!": "You guessed the winner!",
    "The gainings amounted to": "The gainings amounted to",
    "At the moneybox now": "At the moneybox now",
    "Eah": "Eah",
    "The bet did not work": "The bet didn't work",
    "fight": "duel",
    "participants": "participants",
    "competitors": "competitors",
    "successful was strike by": "The goal was reached by the strike of the fighter",
    "Strike by": "Strike by",
    "Dice is": "Dice is",
    "He did damage equal to": "He did damage equal to",
    "Armor of": "Armor of",
    "is now equal to": "is now equal to",
    "the winner is": "the winner is",
    "won the tournament": "won the tournament",
    "You guessed the winner of the tournament!": "You guessed the winner of the tournament!",
    "The gain is": "The gain is",
    "Total in the moneybox": "Total in the moneybox",
    "Your bet was on the fighter": "Your bet was on the fighter",
    "You didn't win anything for the tournament.": "You didn't win anything for the tournament.",
    "Your winnings for the tournament": "Your winnings for the tournament",
    "Your tournament loss": "Your tournament loss",
    "As a result of the tournament, the moneybox reached":
        "As a result of the tournament, the moneybox reached",
    "And this is a new record high!": "And this is a new record high!",
    "The final checkout": "The final checkout",
    "You are on the leaderboard! Enter your name:": "You are on the leaderboard! Enter your name:",
    "You are out of the leaderboard": "You are out of the leaderboard.",
    "You have moved up to": "You have moved up to",
    "th place": "th place",
    "You have moved down to": "You have moved down to",
    "You have remained in the same place in the leaderboard.":
        "You have remained in the same place in the leaderboard.",
    "versus": "versus",
}

RUSSIAN_LOCALIZE_DICT = {
    "greeting message": "Приветствуем на турнире!",
    "continue message": "Продолжим еще одним турниром?",
    "close window request": 'Для закрытия окна введите "да" или "нет"',
    "number of fighters request": "Сколько бойцов будет сражаться?",
    "incorrect! Only": "Нипанятна вводишь. Только",
    "please": "пожалуйста",
    "Shall we give name to the fighters?": "Будем давать имя бойцам?",
    "Will we give the next fighter a name?": "Следующему бойцу будем задавать имя?",
    "If not, it will be set randomly": "Если нет, оно будет задано случайным образом",
    "yes/no": "да/нет",
    "What name will we give to fighter #": "Какое имя дадим бойцу №",
    "or": "или",
    "what character sets will we use?": "Каких бойцов наберем? Можно несколько:",
    "spaces and punctuation are ignored": "пробелы и знаки препинания игнорируются",
    "error message for choose name list": "Ввод не распознан. Только цифры из набора",
    "will we set parameters for this fighter?":
        "А параметры для него задавать будем? (Если нет, они будут заданы случайным образом)",
    "set parameter type for the fighter": "Какой параметр задаем для бойца",
    "set parameter category": "Каков по значению будет параметр",
    "for the fighter": "для бойца",
    "The following fighters compete at the tournament:": "На турнире выступают:",
    "Fighter": "Боец",
    "versus fighter": "бойца",
    "request for the winner of the tournament":
        "Поставим прямо сейчас на победителя турнира? \nЕсли он всех победит, ставка увеличится в",
    "times": "раз",
    "timess": "раза",
    "request for bet for the winner of the fight": "Поставим на кого-то из них?",
    "If he wins the fight, the bet will increase by": "Если он выиграет бой, ставка увеличится в",
    "answer options": "Варианты ответов",
    "request for name for bet": "На кого поставим?",
    "error options choose fighter for bet":
        "Нипанятна вводишь. Только номер или имя бойца, пожалуйста:",
    "bet value request": "Сколько ставим?",
    "you have at your disposal": "в распоряжении",
    "error options for choose bet value with input type":
        "Вводим целое число. Только целое, только число!",
    "error options for choose bet value with input interval":
        "Ставка должна быть больше ноля, конечно!",
    "error options for choose bet value with money-box size":
        "Нет у тебя столько денег. Меньше ставь!",
    "Bets accepted!": "Ставка принята!",
    "for fighter": "на бойца",
    "left in your moneybox": "Остаток банка",
    "If he wins, you win": "Если он победит, выиграете",
    "best parameter": "лучший параметр",
    "but worst": "но худший",
    "but he probably": "но он вероятно",
    "very": "очень",
    "and": "и",
    "probably": "возможно",
    "duelling": "уровень фехтования",
    "might": "сила",
    "armor": "броня",
    "low": "низкий",
    "normal": "средний",
    "high": "высокий",
    "dexterous": "умелый",
    "strong": "силен",
    "steel-clad": "бронирован",
    "unskillful": "увалень",
    "weak": "слабак",
    "exposed": "голый",
    "You guessed the winner!": "Вы угадали победителя!",
    "The gainings amounted to": "Выигрыш составил",
    "At the moneybox now": "В банке теперь",
    "Eah": "Эх",
    "The bet did not work": "Ставка не сыграла",
    "fight": "поединок",
    "participants": "дерутся",
    "competitors": "участники",
    "successful was strike by": "Цели достиг удар бойца",
    "Strike by": "Удар",
    "Dice is": "Бросок на",
    "He did damage equal to": "Он нанес урон на",
    "Armor of": "Броня бойца",
    "is now equal to": "теперь",
    "the winner is": "победил",
    "won the tournament": "выиграл турнир",
    "You guessed the winner of the tournament!": "Офигеть! Вы угадали победителя турнира!",
    "The gain is": "Выигрыш",
    "Total in the moneybox": "Итого в банке",
    "Your bet was on the fighter": "А ставили вы на бойца",
    "You didn't win anything for the tournament.": "За турнир ничего не выиграли.",
    "Your winnings for the tournament": "За турнир вы выиграли",
    "Your tournament loss": "За турнир вы проиграли",
    "As a result of the tournament, the moneybox reached": "По итогу турнира касса достигла",
    "And this is a new record high!": "И это новый рекорд!",
    "The final checkout": "Итоговая касса",
    "You are on the leaderboard! Enter your name:": "Вы вошли в таблицу рекордов! Ведите свое имя:",
    "You are out of the leaderboard": "Вы вылетели из таблицы рекордов.",
    "You have moved up to": "Вы поднялись в таблице на",
    "th place": " место",
    "You have moved down to": "Вы опустились на",
    "You have remained in the same place in the leaderboard.":
        "Вы остались на том же месте в таблице рекордов.",
    "versus": "против",
}

NamesCollection = namedtuple(
    "NamesCollections", ["localized_description", "characters_sets"]
)

# Tuples with sets for creating fighters. Each set is a tuple with the structure:
# index 0 - str[name], index 1 - str[type of specified parameter
# (parameter_type from PARAMETERS_DELTAS)],
# index 2 - str[category of value of specified parameter
# (parameter_category from CATEGORIES_LIMITS)]).
# The name of the tuple is used as a description when the player selects character sets.
# Кортежи c наборами для создания бойцов. Каждый набор - кортеж со структурой:
# (index 0 - str[имя], index 1 - str[тип заданного параметра (parameter_type из PARAMETERS_DELTAS)],
# index 2 - str[категория величины заданного параметра (parameter_category из CATEGORIES_LIMITS)]).
# Имя списка используется в качестве описания при выборе игроком наборов персонажей.

ENG_NAME_LIST_HEROES = NamesCollection(
    "heroes from legends and fiction",
    (
        ("Robin Hood", "duelling", "high"),
        ("Heracles", "might", "high"),
        ("Samson", "armor", "high"),
        ("d'Artagnan", "duelling", "high"),
        ("Geralt of Rivia", "duelling", "high"),
        ("Aragorn", "duelling", "high"),
        ("Yoda", "duelling", "high"),
        ("Connor MacLeod", "duelling", "high"),
        ("Porthos", "might", "high"),
        ("El Cid Campeador", "armor", "high"),
        ("Ilya Muromets", "might", "high"),
        ("Alyosha Popovich", "armor", "high"),
        ("Dobrynya Nikitich", "duelling", "high"),
        ("Svyatogor", "might", "high"),
        ("King Arthur", "armor", "high"),
        ("Lancelot of the Lake", "duelling", "high"),
        ("Tristan", "duelling", "high"),
        ("Batman", "armor", "high"),
        ("Spider-Man", "duelling", "high"),
        ("Hulk", "might", "high"),
        ("Achilles", "armor", "high"),
        ("Perseus", "duelling", "high"),
        ("Beowulf", "might", "high"),
        ("Ajax the Great", "might", "high"),
        ("Cú Chulainn", "might", "high"),
        ("Diarmid O'Dyna", "duelling", "high"),
        ("Muirchertach Mac Ercae", "armor", "high"),
        ("Diomedes", "duelling", "high"),
        ("Sigurd", "armor", "high"),
        ("Polyphemus", "might", "high"),
        ("Fionn mac Cumhaill", "duelling", "high"),
        ("Conan the Barbarian", "might", "high"),
        ("Elrond", "duelling", "high"),
        ("Boromir", "armor", "high"),
        ("Legolas", "duelling", "high"),
        ("Gimli", "armor", "high"),
        ("Thorin Oakenshield", "armor", "high"),
        ("Captain Alatriste", "duelling", "high"),
        ("Roland", "armor", "high"),
        ("Hector", "might", "high"),
        ("Manas Baghatur", "might", "high"),
        ("Pan Volodyovski", "duelling", "high"),
        ("Richard Sharpe", "duelling", "high"),
        ("Alpamysh Baghatur", "might", "high"),
    ),
)

RUS_NAME_LIST_HEROES = NamesCollection(
    "герои из легенд",
    (
        ("Робин Гуд", "duelling", "high"),
        ("Геракл", "might", "high"),
        ("Самсон", "armor", "high"),
        ("Д'Артаньян", "duelling", "high"),
        ("Волкодав", "duelling", "high"),
        ("Геральт из Ривии", "duelling", "high"),
        ("Арагорн", "duelling", "high"),
        ("Магистр Йода", "duelling", "high"),
        ("Дон Румата Эсторский", "duelling", "high"),
        ("Коннор Маклауд", "duelling", "high"),
        ("Портос", "might", "high"),
        ("Эль Сид Камеадор", "armor", "high"),
        ("Илья Муромец", "might", "high"),
        ("Алеша Попович", "armor", "high"),
        ("Добрыня Никитич", "duelling", "high"),
        ("Святогор", "might", "high"),
        ("Король Артур", "armor", "high"),
        ("Ланселот", "duelling", "high"),
        ("Тристан", "duelling", "high"),
        ("Бетмен", "armor", "high"),
        ("Человек-паук", "duelling", "high"),
        ("Халк", "might", "high"),
        ("Ахилл", "armor", "high"),
        ("Персей", "duelling", "high"),
        ("Беовульф", "might", "high"),
        ("Аякс", "might", "high"),
        ("Кухулин", "might", "high"),
        ("Диармайд О'Дина", "duelling", "high"),
        ("Муйрхертах", "armor", "high"),
        ("Диомед", "duelling", "high"),
        ("Сигурд", "armor", "high"),
        ("Полифем", "might", "high"),
        ("Финн МакКумал", "duelling", "high"),
        ("Конан-Варвар", "might", "high"),
        ("Никита Кожемяка", "might", "high"),
        ("Элронд", "duelling", "high"),
        ("Боромир", "armor", "high"),
        ("Леголас", "duelling", "high"),
        ("Гимли", "armor", "high"),
        ("Торин Дубощит", "armor", "high"),
        ("Капитан Алатристе", "duelling", "high"),
        ("Роланд", "armor", "high"),
        ("Гектор Приамид", "might", "high"),
        ("Пересвет", "duelling", "high"),
        ("Челубей", "might", "high"),
        ("Манас-батыр", "might", "high"),
        ("пан Володыевский", "duelling", "high"),
        ("Ричард Шарп, королевский стрелок", "duelling", "high"),
        ("Алпамыш-батыр", "might", "high"),
    ),
)

ENG_NAME_LIST_REAL = NamesCollection(
    "historical great fighters",
    (
        ("Evpaty Kolovrat", "duelling", "high"),
        ("Ivan Poddubny", "might", "high"),
        ("Spartacus", "duelling", "high"),
        ("Crixus", "might", "high"),
        ("Gannicus", "duelling", "high"),
        ("Ragnar Lodbrok", "duelling", "high"),
        ("Rolf the Ganger", "might", "high"),
        ("Yermak Timofeyevich", "armor", "high"),
        ("Alaric I Visigoth", "might", "high"),
        ("William Wallace", "armor", "normal"),
        ("Sviatoslav I Igorevich", "duelling", "high"),
        ("Eric Bloodaxe", "duelling", "high"),
        ("Arminius", "might", "high"),
        ("Richard the Lionheart", "armor", "high"),
        ("Leonidas I", "duelling", "high"),
        ("Alexander the Great", "armor", "high"),
        ("William Marshal", "armor", "high"),
        ("Yue Fei", "duelling", "high"),
        ("Dmitry Bobrok", "armor", "high"),
        ("Mstislav the Daring", "duelling", "high"),
        ("Alexander Popovich of Rostov", "armor", "high"),
        ("Mstislav the Brave", "armor", "high"),
        ("Denis Davydov", "duelling", "high"),
        ("Mikhail Skopin-Shuisky", "armor", "high"),
        ("Bertrand du Guesclin", "armor", "high"),
        ("Henry of Portugal", "duelling", "high"),
        ("Miyamoto Musashi", "duelling", "high"),
        ("Chevalier d'Éon", "duelling", "high"),
        ("Minamoto no Yoshitsune", "duelling", "high"),
        ("Donald McBane", "duelling", "high"),
        ("Johannes Liechtenauer", "duelling", "high"),
        ("Itō Ittōsai", "duelling", "high"),
        ("Louis de Bussy d'Amboise", "duelling", "high"),
        ("Cyrano de Bergerac", "duelling", "high"),
        ("Milo of Croton", "might", "high"),
        ("Diagoras of Rhodes", "might", "high"),
        ("Polydamas of Skotoussa", "might", "high"),
        ("Vercingetorix", "armor", "high"),
        ("Basil II Porphyrogenitus", "armor", "high"),
        ("Flamma", "duelling", "high"),
        ("Lü Bu", "armor", "high"),
        ("Bohemond I of Antioch", "armor", "high"),
        ("Tancred of Galilee", "might", "high"),
        ("Pierre Terrail de Bayard ", "armor", "high"),
    ),
)

RUS_NAME_LIST_REAL = NamesCollection(
    "исторические великие бойцы",
    (
        ("Евпатий Коловрат", "duelling", "high"),
        ("Иван Поддубный", "might", "high"),
        ("Спартак", "duelling", "high"),
        ("Крикс Галл", "might", "high"),
        ("Гай Ганник", "duelling", "high"),
        ("Рагнар Лодброк", "duelling", "high"),
        ("Хрольв Пешеход", "might", "high"),
        ("Ермак", "armor", "high"),
        ("Аларих Варвар", "might", "high"),
        ("Уильям Уоллес", "armor", "normal"),
        ("Святослав Игоревич", "duelling", "high"),
        ("Эйрик Кровавая Секира", "duelling", "high"),
        ("Арминий", "might", "high"),
        ("Ричард Львиное Сердце", "armor", "high"),
        ("Леонид", "duelling", "high"),
        ("Александр Македонский", "armor", "high"),
        ("Уильям Маршалл", "armor", "high"),
        ("Юэ Фей", "duelling", "high"),
        ("Дмитрий Боброк Волынский", "armor", "high"),
        ("Мстислав Удатный", "duelling", "high"),
        ("Петр Кошка", "duelling", "high"),
        ("Александр Попович", "armor", "high"),
        ("Добрыня Златой Пояс", "duelling", "high"),
        ("Нефедий Дикун", "might", "high"),
        ("Мстислав Храбрый", "armor", "high"),
        ("Ян Усмошвец", "might", "high"),
        ("Козьма Крючков", "duelling", "high"),
        ("Леонтий Коренной", "duelling", "high"),
        ("Михаил Скопин-Шуйский", "armor", "high"),
        ("Бертран дю Геклен", "armor", "high"),
        ("Генрих Бургундский", "duelling", "high"),
    ),
)

RUS_NAME_LIST_JOKE = NamesCollection(
    "повеселиться",
    (
        ("Навуходоносор", "armor", "high"),
        ("Абизян", "duelling", "high"),
        ("Мегатрон", "might", "high"),
        ("Мегабубон", "armor", "high"),
        ("Кто на новенького?", "duelling", "normal"),
        ("Подлый Трус", "might", "low"),
        ("Кропоткин", "duelling", "low"),
        ("Фараон пустоты", "duelling", "low"),
        ("Крокодил", "might", "high"),
        ("Лаптемастер", "duelling", "normal"),
        ("Петеволк", "armor", "low"),
        ("Ледокол Путезоба", "might", "high"),
        ("Человек и пароход", "duelling", "low"),
        ("Лохмастер", "might", "low"),
        ("Фантастик-Печкин", "armor", "low"),
        ("Чугунный мост", "duelling", "low"),
        ("Чехлы от Боинга", "might", "normal"),
        ("Коптилкин", "duelling", "low"),
        ("Мегачел", "duelling", "normal"),
        ("Забияка", "might", "normal"),
        ("Дразнилкин", "might", "normal"),
        ("Крутолох", "armor", "low"),
        ("Доктор Пилюлькин", "might", "high"),
        ("Грустный Жулик", "might", "low"),
        ("Лысый Жирик", "might", "low"),
        ("Жирный Лысик", "might", "low"),
        ("Вуглускр", "duelling", "high"),
        ("Лень-Неохота", "duelling", "low"),
        ("Чипиздрик", "duelling", "high"),
        ("Синьор-Помидор", "armor", "high"),
        ("Ниндзя Чипполино", "duelling", "high"),
        ("ГераКакл", "might", "high"),
        ("Бармаглот", "duelling", "high"),
        ("Хливкие Шорьки", "armor", "low"),
    ),
)

ENG_NAME_LIST_WALES = NamesCollection(
    "historical and legendary heroes of Wales and Cornwall",
    (
        ("Cunedda ap Edern", "duelling", "high"),
        ("Macsen Wledig", "armor", "high"),
        ("Vortigern", "might", "high"),
        ("Llywelyn the Great", "duelling", "high"),
        ("Llywelyn the Last", "armor", "high"),
        ("The Lord Rhys", "might", "high"),
        ("Gilbert de Clare", "armor", "high"),
        ("Richard Strongbow", "duelling", "high"),
        ("Mark of Cornwall", "armor", "high"),
        ("Pwyll of Dyfed", "duelling", "high"),
        ("Math ap Mathonwy", "might", "high"),
        ("Culhwch ap Cilydd", "might", "high"),
        ("Uther Pendragon", "might", "high"),
        ("Gorlois of Cornwall", "armor", "high"),
        ("Owain mab Urien", "duelling", "high"),
        ("Ysbaddaden Chief of Giants", "might", "high"),
        ("Glewlwyd Gafaelfawr", "might", "high"),
        ("Cei ap Cynyr seneschal", "armor", "high"),
        ("Bedwyr", "might", "high"),
        ("Gwalchmai", "duelling", "high"),
        ("Cador of Cornwall", "duelling", "high"),
        ("Seithenyn", "might", "high"),
        ("Tristan", "duelling", "high"),
        ("Morholt of Ireland", "might", "high"),
        ("Meliodas", "duelling", "high"),
        ("Tutwal ap Guoremor", "duelling", "high"),
        ("Conan Meriadoc", "duelling", "high"),
        ("Brychan Brycheiniog", "duelling", "high"),
        ("Brian of Brittany", "duelling", "high"),
        ("Dyfnwal Boifunall ap Ithel", "duelling", "high"),
        ("Rhodri Molwynog", "armor", "high"),
        ("Maelgwn Gwynedd", "might", "high"),
        ("Rhodri the Great", "armor", "high"),
        ("Owain Gwynedd", "duelling", "high"),
        (" Owen Glendower", "duelling", "high"),
    ),
)

RUS_NAME_LIST_WALES = NamesCollection(
    "исторические и легендарные герои Уэльса и Корнуолла",
    (
        ("Кунедда ап Эдерн", "duelling", "high"),
        ("Максен Вледиг", "armor", "high"),
        ("Вортигерн", "might", "high"),
        ("Лливелин Великий", "duelling", "high"),
        ("Лливелин Последний", "armor", "high"),
        ("Рис ап Гриффид", "might", "high"),
        ("Гилберт де Клер", "armor", "high"),
        ("Ричард Строгнбоу де Клер", "duelling", "high"),
        ("Марк Корнубский", "armor", "high"),
        ("Пуйл князь Диведа", "duelling", "high"),
        ("Мат ап Матонви", "might", "high"),
        ("Килух ап Килидд", "might", "high"),
        ("Утер Пендрагон", "might", "high"),
        ("Горлой Корнубский", "armor", "high"),
        ("Овейн ап Уриен", "duelling", "high"),
        ("Ысбаддаден Великан-из-Великанов", "might", "high"),
        ("Глевлвид Могучая хватка", "might", "high"),
        ("Кай ап Кинир сенешаль", "armor", "high"),
        ("Бедуир", "might", "high"),
        ("Гвалхмей", "duelling", "high"),
        ("Кадур ярл Корнуолла", "duelling", "high"),
        ("Сэйтеннин", "might", "high"),
        ("Тристан ап Мелиодас", "duelling", "high"),
        ("Морхульт", "might", "high"),
        ("Мелиодас ап Фелек", "duelling", "high"),
        ("Тутвал ап Гворемор", "duelling", "high"),
        ("Кинан Мериадок", "duelling", "high"),
        ("Брихан из Брекнока", "duelling", "high"),
        ("Бриан Бретонский", "duelling", "high"),
        ("Дивнуал ап Ител", "duelling", "high"),
        ("Родри ап Идвал", "armor", "high"),
        ("Майлгун Высокий ап Кадваллон", "might", "high"),
        ("Родри Великий ап Мервин", "armor", "high"),
        ("Оуайн Глиндур ап Грифид", "duelling", "high"),
        ("Оуайн IV Глиндур", "duelling", "high"),
    ),
)

# Initial leaderboard
# Начальный список рекордов
ENGLISH_HIGH_SCORES = {
    "Tigger": 1000,
    "Cheshire Cat": 750,
    "Scrooge McDuck": 190,
    "Daffy Duck": 650,
    "Hedgehog in the Fog": 500,
    "Tooth fairy": 400,
    "Bugs Bunny": 320,
    "Piglet": 250,
    "Cheburashka": 140,
    "Winnie-the-Pooh": 110,
}

RUSSIAN_HIGH_SCORES = {
    "Тигра": 1000,
    "Кот Матроскин": 750,
    "Почтальон Печкин": 190,
    "Каркуша": 650,
    "Ежик-в-Тумане": 500,
    "Старуха Шапокляк": 400,
    "Степашка": 320,
    "Пятачок": 250,
    "Чебурашка": 140,
    "Винни-Пух": 110,
}

# Response options to the request to enter the answer in the format 'yes'/'no'
# Варианты ответов на просьбу ввести ответ в формате 'да'/'нет'
ANSWER_OPTIONS_YES_NO_RUS_ENG = (
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
    ),
    (
        "нет",
        "0",
        "n",
        "не",
        "ytn",
        "неа",
        "отвали",
        "нафиг",
        "на фиг",
        "no",
        "nah",
        "nope",
        "nay",
    ),
)

# Input error message options for a yes/no question. After each error, the next option is displayed.
# When the options run out, the last option is displayed each time.
# Варианты сообщений об ошибке ввода на вопрос, требующий ответа 'да'/'нет'.
# После каждой ошибки выводится следующий вариант. Когда варианты заканчиваются,
# выводится каждый раз последний вариант.
ENG_ERROR_OPTIONS_YES_NO = (
    'Only "yes" or "no", please:',
    'It will not work. Only "yes" or "no":',
    "The answer is not clear, please try again:",
)

RUS_ERROR_OPTIONS_YES_NO = (
    'Только "да" или "нет", пожалуйста:',
    'Не прокатит. Только "да" или "нет":',
    "Ответ не ясен, повторите ввод, пожалуйста:",
)

# Variants of error messages in case of an unreadable response to a request to choose
# from which sets of characters the list of fighters is formed.
# Варианты сообщений об ошибке при нечитаемом ответе на просьбу выбрать
# из каких наборов персонажей формируется список бойцов.
ENG_ERROR_MESSAGES_FOR_OPTIONS = (
    "Enter the number! Let's go from the beginning!",
    "Still need a variant number. Let's repeat the step!",
    "Joke, right?",
    "What is difficult? You need a number!",
    "Are you kidding me?",
    "Don't annoy me!",
    "Aaaaaaaa!!! [roaring] Please, please!",
    "Just enter any number, number: 1, 2, etc. by option number",
)

RUS_ERROR_MESSAGES_FOR_OPTIONS = (
    "Число вводим! Поехали с начала!",
    "Все-таки нужен номер варианта. Повторяем этап!",
    "Шутка, да?",
    "Чего сложного-то? Номер надо!",
    "Ну хватит уже! Вводи как просят!",
    "Издеваешься?",
    "Не беси меня!",
    "Сука!!!!",
    "Аааааааа!!! [ревет] Ну, пожалуйста, пожалуйста!",
    "Просто введи любое число, цифру: 1, 2 и т.п. по номеру варианта",
)

ENG_ROUND_NAMES = {
    2: "Final",
    4: "Semifinals",
    8: "Quarterfinals",
    16: "Eighth-finals",
    32: "16th-finals",
}

RUS_ROUND_NAMES = {
    2: "Финал",
    4: "Полуфиналы",
    8: "Четверьфиналы",
    16: "1/8 финала",
    32: "1/16 финала",
}

# user's response options when choosing a bet on the first fighter
# варианты ответов пользователя при выборе ставки на первого бойца
ENG_FIRST_FIGHTER_OPTIONS = (
    "1",
    "first",
    "one",
    "earliest",
    "prime",
    "alpha",
    "fore",
    "leading",
    "a",
    "1st",
    "chief",
)

RUS_FIRST_FIGHTER_OPTIONS = (
    "1",
    "первый",
    "gthdsq",
)

# user's response options when choosing a bet on the second fighter
# варианты ответов пользователя при выборе ставки на второго бойца
ENG_SECOND_FIGHTER_OPTIONS = (
    "2",
    "second",
    "secondary",
    "other",
    "alternative",
    "b",
    "2nd",
    "deutero",
    "two",
    "secondly",
    "secundus",
    "latter",
    "another",
    "bravo",
    "beta",
    "betta",
)

RUS_SECOND_FIGHTER_OPTIONS = (
    "2",
    "второй",
    "dnjhjq",
)

# Description of the results of strikes during combat
# Описание результатов ударов во время боя
ENG_STRIKE_RESULT_OPTIONS = {
    "kiss": "They are kissing! But now they strike again!",
    "compensation": "The strike is parried!",
    "miss": "Both missed. Beat again!",
}

RUS_STRIKE_RESULT_OPTIONS = {
    "kiss": "Они целуются! Но вот бьют снова!",
    "compensation": "Удар парирован!",
    "miss": "Оба промахнулись. Бьют снова!",
}

# dictionary of descriptions of parameters having the lowest value
# словарь описания параметров, имеющих низшее значение
WORSE_EPITHETS_DICT = {
    "duelling": "unskillful",
    "might": "weak",
    "armor": "exposed",
}

# dictionary describing the parameters with the highest value
# словарь описания параметров, имеющих наивысшее значение
BEST_EPITHETS_DICT = {
    "duelling": "dexterous",
    "might": "strong",
    "armor": "steel-clad",
}

# sets of localized dictionaries for each localization option
# наборы локализованных словарей для каждого варианта локализации
DICT_VARIANT = {
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
    "RUS": {
        "LOCALIZE_DICT": RUSSIAN_LOCALIZE_DICT,
        "GENERAL_NAME_LIST": (
            RUS_NAME_LIST_HEROES,
            RUS_NAME_LIST_REAL,
            RUS_NAME_LIST_JOKE,
            RUS_NAME_LIST_WALES,
        ),
        "HIGH_SCORES": RUSSIAN_HIGH_SCORES,
        "ANSWER_OPTIONS_YES_NO": ANSWER_OPTIONS_YES_NO_RUS_ENG,
        "ERROR_OPTIONS_YES_NO": RUS_ERROR_OPTIONS_YES_NO,
        "ERROR_MESSAGES_FOR_OPTIONS": RUS_ERROR_MESSAGES_FOR_OPTIONS,
        "ROUND_NAMES": RUS_ROUND_NAMES,
        "FIRST_FIGHTER_OPTIONS": RUS_FIRST_FIGHTER_OPTIONS,
        "SECOND_FIGHTER_OPTIONS": RUS_SECOND_FIGHTER_OPTIONS,
        "STRIKE_RESULT_OPTIONS": RUS_STRIKE_RESULT_OPTIONS,
    },
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
    },
}

# Switch between localization options. Change only it and the entire user interface
# will be localized. For English, use the value 'ENG'
# Переключатель между вариантами локализации. Поменяйте только его и весь интерфейс общения
# с пользователем будет локализован. Для английского языка используйте значение 'ENG'
choosen_language = "ENG"

# Formation of operational messages for the user based on the selected localization option
# (the choosen_language variable) and a set of localization dictionaries (dictionary DICT_VARIANT)
# Формирование рабочих сообщений для пользователя на основе выбранного варианта локализации
# (переменная choosen_language) и набора словарей локализации (словарь DICT_VARIANT)
LOCALIZE_DICT = {
    key: DICT_VARIANT[choosen_language]["LOCALIZE_DICT"][key]
    for key in ENGLISH_LOCALIZE_DICT
}

GENERAL_NAME_LIST = DICT_VARIANT[choosen_language]["GENERAL_NAME_LIST"]

HIGH_SCORES = DICT_VARIANT[choosen_language]["HIGH_SCORES"]

ANSWER_OPTIONS_YES_NO = DICT_VARIANT[choosen_language]["ANSWER_OPTIONS_YES_NO"]

ERROR_OPTIONS_YES_NO = DICT_VARIANT[choosen_language]["ERROR_OPTIONS_YES_NO"]

ERROR_MESSAGES_FOR_OPTIONS = DICT_VARIANT[choosen_language]["ERROR_MESSAGES_FOR_OPTIONS"]

ROUND_NAMES = DICT_VARIANT[choosen_language]["ROUND_NAMES"]

FIRST_FIGHTER_OPTIONS = DICT_VARIANT[choosen_language]["FIRST_FIGHTER_OPTIONS"]

SECOND_FIGHTER_OPTIONS = DICT_VARIANT[choosen_language]["SECOND_FIGHTER_OPTIONS"]

STRIKE_RESULT_OPTIONS = DICT_VARIANT[choosen_language]["STRIKE_RESULT_OPTIONS"]
