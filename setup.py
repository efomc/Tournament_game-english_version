from setuptools import setup, find_packages

import tournament_game

install_requires = [
    'pytest>=6.2.5',
    'setuptools>=56.0.0',
]

setup(
    name='Tournament_game',
    version=tournament_game.__version__,
    license='MIT License',
    packages=find_packages(),
    description='fight tournament game',
    long_description=(
        'The Tournament_game simulates a tournament between different fighters, '
        'with the ability to choose fighters from different lists, create your own characters, '
        'bet on the outcome of the fights or the tournament.'),

    author='Egor Fomin, beresk_let',
    author_email='fomc@inbox.ru',
    url='https://github.com/efomc/',

    entry_points={
        'console_scripts':
            ['tournamentgame = tournament_game.core:main']
        },

    test_suite='tests',
)



