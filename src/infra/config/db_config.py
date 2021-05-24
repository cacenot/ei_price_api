from mongoengine import connect, disconnect_all

from src.settings import Settings


class DBConnectionHandler:

    def __init__(self):
        self.__connection_string = Settings.MONGODB_HOST

    def __enter__(self):
        connect(host=self.__connection_string)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        disconnect_all()
