

class NewUserRequest:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username


class NewMessageRequest:
    def __init__(self, token: str, message: str):
        self.__token = token
        self.__message = message

    @property
    def token(self):
        return self.__token

    @property
    def message(self):
        return self.__message
