from datetime import datetime
import enum


class MessageType(enum.Enum):
    INFO = 0
    STATUS = 1
    WARNING = 2
    ERROR = 3


class LogMessage:
    def __init__(self, msg_type: MessageType, message: str, func: str, func_res: str = None, *func_args, **func_kwargs):
        self.__time = datetime.now()
        self.__msg_type = msg_type
        self.__message = message
        self.__func = func
        self.__func_res = func_res
        self.__func_args = func_args
        self.__func_kwargs = func_kwargs

    def __str__(self):
        res = f'[{self.__time}][{self.__msg_type.name}]: Викликано функцію: {self.__func}'

        if self.__message is not None:
            res += f', {self.__message}'

        if self.__func_res is not None:
            res += f', результат функції: {self.__func_res}'

        return res
