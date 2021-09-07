from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State

import api
from loader import dp

URL = 'url'

wait_url_name = State('wait_url_name')


@dp.message_handler()
async def ask_url_name(msg: types.Message, state: FSMContext):
    await state.update_data({URL: msg.text})
    await wait_url_name.set()
    await msg.answer('Придумай название для этой ссылки')


@dp.message_handler(state=wait_url_name)
async def ask_url_name(msg: types.Message, state: FSMContext):
    sdata = await state.get_data()

    try:
        short_url = await api.get_short_url(sdata[URL], msg.text)
    except api.NameDuplicateError:
        await msg.answer('Это название уже занято')
    else:
        await state.finish()
        await msg.answer(short_url)
