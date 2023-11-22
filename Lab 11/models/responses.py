class NewUserResponse:
    def __init__(self, token, messages):
        self.__token = token
        self.__messages = messages

    @property
    def token(self):
        return self.__token

    @property
    def messages(self):
        return self.__messages


class ErrorResponse:
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

    @property
    def message(self):
        return self.__message
