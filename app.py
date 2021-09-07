from aiogram import executor

from loader import dp


async def on_startup(_):
    import handlers
    import middlewares

    handlers.setup()
    middlewares.setup()


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)
