from typing import List


list_counter: List[str] = []


def score_counter(lst: List[str]) -> dict:
    number_draw = lst.count('nobody_won')
    number_user_wins = lst.count('user_won')
    number_bot_wins = lst.count('bot_won')
    result_score_counter = f'Счет серии игр "Камень-Ножницы-Бумага"' \
                           f'\n\nПобед игрока: {number_user_wins}' \
                           f'\n\nПобед бота: {number_bot_wins}' \
                           f'\n\nСыграно в ничью: {number_draw}'
    lst = []
    number_draw, number_user_wins, number_bot_wins = 0, 0, 0
    return result_score_counter
