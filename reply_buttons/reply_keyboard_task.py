from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
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
buttons: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in range(1, 13)
]

# Инициализируем билдер
builder = ReplyKeyboardBuilder()

# builder.row(*buttons, width=3) # этот билдер построит клавиатуру с 3 кнопками в строке
builder.add(*buttons)
builder.adjust(4, 2, repeat=True) # этот билдер построит клавиатуру с повторяющимися строками 4 кнопки, 2 кнопки, затем опятьь 4 и 2

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем с обычными кнопками',
        reply_markup=my_keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
