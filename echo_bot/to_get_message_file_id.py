import  json

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
    await message.answer('Привет!\nМеня зовут Get file_id bot!\nпришли мне сообщение и я отправлю тебе тип сообщения и его file_id')





# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start"
@dp.message()
async def to_get_message_file_id(message: Message):

    if message.photo:
        photo_id = message.photo[0].file_id
        await message.answer(text=f'photo_id = {photo_id}')
        print(f'photo_id = {photo_id}')

    elif message.video:
        video_id = message.video.file_id
        await message.answer(text=f'video_id = {video_id}')
        print(f'video_id = {video_id}')

    elif message.document:
        document_id = message.document.file_id
        await message.answer(text=f'document_id = {document_id}')
        print(f'document_id = {document_id}')

    elif message.audio:
        audio_id = message.audio.file_id
        await message.answer(text=f'audio_id = {audio_id}')
        print(f'audio_id = {audio_id}')

    elif message.voice:
        voice_id = message.voice.file_id
        await message.answer(text=f'voice_id = {voice_id}')
        print(f'voice_id = {voice_id}')

    elif message.animation:
        animation_id = message.animation.file_id
        await message.answer(text=f'animation_id = {animation_id}')
        print(f'animation_id = {animation_id}')

if __name__ == '__main__':
    dp.run_polling(bot)