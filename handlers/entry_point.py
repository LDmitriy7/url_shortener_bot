from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands='start', state='*')
async def send_welcome(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Отправь мне ссылку для сокращения')
