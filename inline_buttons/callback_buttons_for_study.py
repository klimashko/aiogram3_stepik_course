# Код в этом модуле повторяет код из callback_buttons_2.py, копировал код из урока в курсе,
# чтобы лучше запомнить материал
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from environs import Env
from aiogram.types import CallbackQuery


# Считываем "BOT TOKEN" HERE из переменных о
env = Env() #Env() создает новый экземпляр класса Env, который предоставляет методы для работы с переменными среды.
env.read_env() #загружает переменные среды из файла .env в объект env
BOT_TOKEN = env.str("BOT_TOKEN") #присваивает переменной BOT_TOKEN значение переменной среды с именем BOT_TOKEN.

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=keyboard
    )

# # Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# #с data 'big_button_1_pressed' или 'big_button_2_pressed'
# #то есть здесь мы ловим апдейт, который возникает,
# # если юзер нажмет на инлайн кнопку с callback_data, то есть callback кнопку
# @dp.callback_query(F.data.in_(['big_button_1_pressed',
#                                'big_button_2_pressed']))
# async def process_buttons_pressed(callback: CallbackQuery):
#     await callback.answer(text='Вы нажали на инлайн кнопку типа callback')

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed' --апдейт на событие -нажата кнопка с text='БОЛЬШАЯ КНОПКА 1'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer('1 lvlrivi')

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed' --апдейт на событие -нажата кнопка с text='БОЛЬШАЯ КНОПКА 2'
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='2 kn;vndkn')


if __name__ == '__main__':
    dp.run_polling(bot)


