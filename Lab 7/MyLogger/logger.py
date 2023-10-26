from .models import MessageType, LogMessage


class Logger:
    def __init__(self):
        self.__logs: list[LogMessage] = list()

    def log(self, log_type: MessageType, message: str = None):
        def decorator_log(func):
            def wrapper(*args, **kwargs):
                try:
                    return_value = func(*args, **kwargs)

                except Exception as e:
                    self.__logs.append(LogMessage(
                        MessageType.ERROR,
                        str(e),
                        func.__name__,
                        None,
                        args,
                        kwargs
                    ))
                    return None

                self.__logs.append(LogMessage(
                    log_type,
                    message,
                    func.__name__,
                    str(return_value),
                    args,
                    kwargs
                ))

                return return_value

            return wrapper

        return decorator_log

    def get_logs(self):
        for i in self.__logs:
            yield i

    def save_to_file(self, filename: str = 'default.log'):
        with open(filename, 'a', encoding='utf-8') as file:
            for i in self.__logs:
                file.write(f'{i}\n')
