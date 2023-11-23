import socket
import pickle
import threading

from models.request import NewUserRequest, NewMessageRequest
from models.responses import NewUserResponse, ErrorResponse
from models.other import Message


class ClientSocket:
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect(('localhost', 12345))

        self.__name = None
        self.__token = None
        self.__messages = []
        self.__new_messages = []

    def __reciever(self):
        while True:
            data_bytes = self.__client.recv(1024)
            obj = pickle.loads(data_bytes)

            if isinstance(obj, Message):
                self.__new_messages.append(obj)

    def login_user(self, name):
        self.__client.send(pickle.dumps(NewUserRequest(name)))

        data_bytes = self.__client.recv(1024)
        obj = pickle.loads(data_bytes)

        if isinstance(obj, NewUserResponse):
            self.__name = name
            self.__token = obj.token
            self.__messages = obj.messages

            threading.Thread(target=self.__reciever).start()

            return None

        elif isinstance(obj, ErrorResponse):
            return obj.message

        else:
            return 'Server exception!'

    def send_message(self, message):
        self.__new_messages.append(Message(self.__name, message))
        self.__client.send(pickle.dumps(NewMessageRequest(self.__token, message)))

    @property
    def messages(self):
        return self.__messages

    @property
    def new_messages(self):
        return self.__new_messages
