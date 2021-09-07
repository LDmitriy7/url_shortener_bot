from aiohttp import web

import config
from loader import bot

API_URL = 'https://my-bots.ru/redirect'

KEY = 'key'
URL = 'url'
TOKEN = 'token'
SHORT_URL = 'short_url'


class NameDuplicateError(Exception):
    pass


async def get_short_url(url: str, name: str):
    params = {TOKEN: config.Api.TOKEN}
    json = {KEY: name, URL: url}

    async with bot.session.post(url=API_URL, params=params, json=json) as resp:
        if resp.status == web.HTTPConflict.status_code:
            raise NameDuplicateError()

        resp_json = await resp.json()
        return resp_json[SHORT_URL]
