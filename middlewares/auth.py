from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import config


class Auth(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(msg: types.Message, *_):
        if msg.from_user.id not in config.Users.ADMINS_IDS:
            await msg.answer('Доступ запрещен.')
            raise CancelHandler
