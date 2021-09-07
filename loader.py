from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
import config
import mongoengine as me

me.connect(
    db=config.Database.NAME,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    host=config.Database.HOST,
    port=config.Database.PORT,
    authentication_source=config.Database.AUTH_SOURCE,
)

storage = MongoStorage(
    db_name=config.Database.NAME,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    host=config.Database.HOST,
    port=config.Database.PORT,
)

bot = Bot(config.Bot.TOKEN)
dp = Dispatcher(bot, storage=storage)
