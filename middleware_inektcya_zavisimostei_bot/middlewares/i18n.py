import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в мидлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        user: User = data.get('event_from_user')
        print("Это переменная user, котрой присвоили data.get('event_from_user')= ", data.get('event_from_user'))

        if user is None:
            return await handler(event, data)

        user_lang = user.language_code
        # user_lang = 'en' #захаркодили язык чтобы был англ
        print('это user_lang присвоили user.language_code -- язык = ' , user.language_code)

        translations = data.get('_translations')

        i18n = translations.get(user_lang)
        if i18n is None:
            data['i18n'] = translations[translations['default']]
            print("если правильно понял, то здесь data['i18n'] присваеваем словарь LEXICON_RU= ", data['i18n'])
        else:
            data['i18n'] = i18n

        logger.debug('Выходим из миддлвари %s', __class__.__name__)

        return await handler(event, data)





