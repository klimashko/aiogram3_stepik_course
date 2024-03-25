from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import (KeyboardButton, KeyboardButtonPollType, Message,
                           ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from environs import Env

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]
]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True,
    one_time_keyboard=True
)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=my_keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)