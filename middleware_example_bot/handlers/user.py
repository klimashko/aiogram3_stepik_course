import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from middleware_example_bot.filters.filters import MyTrueFilter, MyFalseFilter
from middleware_example_bot.lexicon.lexicon import LEXICON_RU

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# Инициализируем роутер уровня модуля
user_router = Router()

# Этот хэндлер срабатывает на команду /start
@user_router.message(MyTrueFilter(), CommandStart())
async def process_start_command(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    # Создаем объект инлайн-кнопки
    button = InlineKeyboardButton(
        text='Кнопка',
        callback_data='button_pressed'
    )
    # Создаем объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])

    # Отправляем сообщение пользователю
    await message.answer(text=LEXICON_RU['/start'], reply_markup=markup)
    logger.debug('Выходим из хэндлера, обрабатывающего команду /start')

# Этот хэндлер срабатывает на нажатие инлайн-кнопки
@user_router.callback_query(F.data, MyTrueFilter())
async def process_button_click(callback: CallbackQuery):
    logger.debug('Вошли в хэндлер, обрабатывающий нажатие на инлайн кнопку')
    await callback.answer(text=LEXICON_RU['button_pressed'])
    logger.debug('Выходим из хэндлера, обрабатывающего нажатие на инлайн-кнопку')

# Это хэндлер, который мог бы срабатывать на любые текстовые сообщения,
# но MyFalseFilter не пропустит апдейты, даже если они будут с текстом.
@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий текст')
    logger.debug('Выходим из хэндлера, обрабатывающего текст')