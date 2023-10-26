from MyLogger.logger import Logger, MessageType

my_logger = Logger()


@my_logger.log(MessageType.INFO)
def multiply(a, b):
    return int(a * b)


print(multiply(1, 5))
print(multiply("dasadsasd", 5))

logs = my_logger.get_logs()
print(next(logs))
print(next(logs))

print(multiply(5154, 5))

print(next(logs))

my_logger.save_to_file()
