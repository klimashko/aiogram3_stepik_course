from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from typing import List
from rock_paper_scissors_bot.keyboards.keyboards import game_kb, yes_no_kb
from rock_paper_scissors_bot.lexicon.lexicon_ru import LEXICON_RU
from rock_paper_scissors_bot.services.services import get_bot_choice, get_winner
from rock_paper_scissors_bot.services.score_service import score_counter, list_counter

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Этот хэндлер срабатывает на команду /stat
@router.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    result_score = score_counter(list_counter)
    await message.answer(result_score)
    list_counter.clear()


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    # score_service
    list_counter.append(winner)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
