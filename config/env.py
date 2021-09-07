import toml

env = toml.load('env.toml')


class Database:
    db = env['Database']

    NAME = db['name']
    HOST = db['host']
    PORT = db['port']
    USERNAME = db.get('username')
    PASSWORD = db.get('password')
    AUTH_SOURCE = db.get('auth_source', 'admin')


class Bot:
    bot = env['Bot']

    TOKEN = bot['token']


class Api:
    api = env['Api']

    TOKEN = api['token']


class Users:
    users = env['Users']

    ADMINS_IDS = users['admins_ids']
