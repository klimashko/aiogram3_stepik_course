from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest
from environs import Env


env = Env() #Env() создает новый экземпляр класса Env, который предоставляет методы для работы с переменными среды.
env.read_env() #загружает переменные среды из файла .env в объект env
BOT_TOKEN = env.str("BOT_TOKEN") #присваивает переменной BOT_TOKEN значение переменной среды с именем BOT_TOKEN.

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIJxGbXj6tApsGmx7uRvCoqdl0yK0XZAAIOAzIbI56YSrb93AABNHzBdAEAAwIAA3MAAzUE',
    'photo_id2': 'AgACAgIAAxkBAAIJxmbXj7Lo3RtEgyIGOtSszb_iF3AUAAIPAzIbI56YSmdr-C6RAAHbEwEAAwIAA3MAAzUE',
    'voice_id1': 'AwACAgIAAxkBAAIJymbXkChB40qtKIh_bO6boqzHHR8fAAKNSwACAYfBSo_ls5h26YqrNQQ',
    'voice_id2': 'AwACAgIAAxkBAAIJzGbXkC4QTHmXEjFBTMtwe_PPDTAVAAKOSwACAYfBSm59ZZZi9UAxNQQ',
    'audio_id1': 'CQACAgIAAxkBAAIJzmbXkDx2MjZFwIRtNeKvU6gPNbKtAAITVQACk0qZStnZOsqJ0jDjNQQ',
    'audio_id2': 'CQACAgIAAxkBAAIJ0GbXkEI6Yd4nyDee2XzmESnZQDhUAAIWVQACk0qZSr2vBrAXo4ZDNQQ',
    'document_id1': 'BQACAgIAAxkBAAIJ0mbXkFF5aPwmpSzWaW3LD-FVYZcDAAIQVQACk0qZSs1egsxOZjtINQQ',
    'document_id2': 'BQACAgIAAxkBAAIJ1GbXkFbNERshUPlEzevpy1f9V9lkAAIRVQACk0qZSiuPg5JBqQH_NQQ',
    'video_id1': 'BAACAgIAAxkBAAIJ1mbXkHWB7NXM92Keu5Z706Dmm2JKAAIVUgACL9aZSoTdmKmV8m-YNQQ',
    'video_id2': 'BAACAgIAAxkBAAIJ2GbXkH01oiy4PbRVYgJiAsCoYqbPAAJCUgACL9aZSghlJDfCymQWNQQ',
}


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'audio')
    await message.answer_audio(
        audio=LEXICON['audio_id1'],
        caption='Это аудио 1',
        reply_markup=markup
    )


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(F.data.in_(
    ['text', 'audio', 'video', 'document', 'photo', 'voice']
))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=LEXICON['video_id2'],
                caption='Это видео 2'
            ),
            reply_markup=markup
        )
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=LEXICON['audio_id1'],
                caption='Это аудио 1'
            ),
            reply_markup=markup
        )


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    await message.answer(text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
