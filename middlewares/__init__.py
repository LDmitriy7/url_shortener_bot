from loader import dp
from .auth import Auth


def setup():
    dp.setup_middleware(Auth())
