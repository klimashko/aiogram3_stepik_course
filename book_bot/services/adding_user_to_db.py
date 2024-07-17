from typing import Union
from aiogram.types import Message, CallbackQuery
from copy import deepcopy
from book_bot.database.database import users_db, user_dict_template


def adding_user_to_db(arg: Union[Message, CallbackQuery]):
    if arg.from_user.id not in users_db:
        users_db[arg.from_user.id] = deepcopy(user_dict_template)
