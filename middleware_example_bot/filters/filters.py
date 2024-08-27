import logging

from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

"""
Фильтры у нас будут фиктивные, то есть один всегда будет возвращать True, 
а второй всегда False, чтобы пронаблюдать разные цепочки выполнения кода. 
В остальном все стандартно для кастомных фильтров в виде классов - 
наследуемся от BaseFilter и определяем метод __call__. 
Внутрь каждого фильтра добавляем лог для наглядности.
"""

logger = logging.getLogger(__name__)


class MyTrueFilter(BaseFilter):
    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return True


class MyFalseFilter(BaseFilter):
    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return False
