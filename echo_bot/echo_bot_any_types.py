import json

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from environs import Env


env = Env() #Env() создает новый экземпляр класса Env, который предоставляет методы для работы с переменными среды.
env.read_env() #загружает переменные среды из файла .env в объект env
BOT_TOKEN = env.str("BOT_TOKEN") #присваивает переменной BOT_TOKEN значение переменной среды с именем BOT_TOKEN.

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        print(message.model_dump_json())
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


if __name__ == '__main__':
    dp.run_polling(bot)