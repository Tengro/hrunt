from typing import Tuple, Union

from . import models


# Register your services here
async def add_user(tg_id: int, chat_id: int, first_name: str) -> Tuple[models.TelegramUser, bool]:
    return await models.TelegramUser.get_or_create(
        tg_id=tg_id, chat_id=chat_id, first_name=first_name
    )
