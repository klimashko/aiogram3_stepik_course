import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from cachetools import TTLCache

CACHE = TTLCache(maxsize=10_000, ttl=5)  # Максимальный размер кэша - 10000 ключей, а время жизни ключа - 5 секунд

logger = logging.getLogger(__name__)

class ThrottlingMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        user: User = data.get('event_from_user')

        if user.id in CACHE:
            return None

        CACHE[user.id] = True

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return await handler(event, data)