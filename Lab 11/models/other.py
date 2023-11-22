class User:
    def __init__(self, connection, username: str, token: str):
        self.__connection = connection
        self.__username = username
        self.__token = token

    @property
    def connection(self):
        return self.__connection

    @property
    def username(self):
        return self.__username

    @property
    def token(self):
        return self.__token


class Message:
    def __init__(self, username: str, message: str):
        self.__username = username
        self.__message = message

    @property
    def username(self):
        return self.__username

    @property
    def message(self):
        return self.__message

    def __str__(self):
        return f'{self.__username}: {self.__message}'
