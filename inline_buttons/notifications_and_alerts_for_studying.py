from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup,
                           Message)
from environs import Env

# Считываем "BOT TOKEN" из переменных окружения
env = Env() #Env() создает новый экземпляр класса Env,
# который предоставляет методы для работы с переменными среды.
env.read_env() #загружает переменные среды из файла .env в объект env
BOT_TOKEN = env.str("BOT_TOKEN") #присваивает переменной BOT_TOKEN
# значение переменной среды с именем BOT_TOKEN.

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


# Этот хэндлер будет мрабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн кнопками
@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки, нажмите на любую)',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(
        text='Ура! Внимание, нажата КНОПКА 1',
        show_alert=True # Аллерт, требующий нажатия на кнопку "OK", чтобы быть убранным.
        # Применяется, чтобы привлечь внимание юзера, чтобы без подтверждения он не мог дальше взаимодействовать с ботом.
    )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Внимание, нажата КНОПКА 2') # внутри всплывающего окна нотификации отображаем текст о том, какая кнопка нажата.


if __name__ == '__main__':
    dp.run_polling(bot)

