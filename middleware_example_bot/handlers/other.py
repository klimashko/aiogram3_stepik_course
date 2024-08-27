import logging

from aiogram import Router
from aiogram.types import Message
from middleware_example_bot.filters.filters import MyTrueFilter, MyFalseFilter
from middleware_example_bot.lexicon.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

# Инициализируем роутер уровня модуля
other_router = Router()

# Этотхэндлер будет срабатывать на любые сообщения,
# кроме тех, для которых есть отдельные хэндлеры
@other_router.message(MyTrueFilter())
async def send_echo(message: Message):
    logger.debug('Вошли в эхо-хэндлер')
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
    logger.debug('Выходим из эхо-хэндлера')