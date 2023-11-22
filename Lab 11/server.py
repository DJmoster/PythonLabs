import logging
import random
import socket
import string
import sys
import threading
import pickle

from models.request import NewUserRequest, NewMessageRequest
from models.responses import NewUserResponse, ErrorResponse
from models.other import User, Message

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s]: %(message)s',
    handlers=(logging.FileHandler(filename='server.log'), logging.StreamHandler(stream=sys.stdout))
)

SERVER_NAME = 'SERVER'

logger = logging.getLogger()
users = []
all_messages = []
users_jobs = []


def generate_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))


def job_executor():
    logger.info('Job executor started!')
    while True:
        if len(users_jobs) != 0:
            for job in users_jobs:
                logger.warning(f'JobExecutor - Started job')
                for user in job[1]:
                    user.connection.send(pickle.dumps(job[0]))
                    logger.info(f'JobExecutor - Sending message to User({user.username})')

                users_jobs.remove(job)
                logger.warning(f'JobExecutor - Job finished')


def create_new_job(new_message: Message, token):
    all_messages.append(new_message)

    job = (new_message, [])
    for i in users:
        if i.token != token:
            job[1].append(i)

    if len(job[1]) != 0:
        logger.warning(f'Created send message job for {len(job[1])} users')
        users_jobs.append(job)


def user_left(user: User):
    logger.warning(f'User({user.username}) left the chat')
    users.remove(user)
    message = Message(SERVER_NAME, f'{user.username} left the chat!')
    create_new_job(message, user.token)


def user_join(user: User):
    logger.warning(f'User({user.username}) joined the chat')
    message = Message(SERVER_NAME, f'{user.username} joined the chat!')
    create_new_job(message, user.token)


def client_thread(conn, addr):
    logger.warning(f'New connection {addr}')

    user = None
    data_bytes = None
    while True:
        try:
            data_bytes = conn.recv(1024)
        except ConnectionResetError:
            user_left(user)
            break

        if data_bytes is None:
            user_left(user)
            break
        try:
            obj = pickle.loads(data_bytes)
        except EOFError:
            break

        if isinstance(obj, NewUserRequest):
            error = False
            for i in users:
                if i.username == obj.username:
                    logger.error(f'{addr} Username({obj.username}) already exist')
                    conn.send(pickle.dumps(ErrorResponse('This username already exist!')))
                    error = True
                    break

            if obj.username == SERVER_NAME:
                logger.error(f'{addr} you cant take server username')
                conn.send(pickle.dumps(ErrorResponse('You cant take this username!')))
                error = True

            if not error:
                token = generate_token()
                user = User(conn, obj.username, token)
                users.append(user)

                response = pickle.dumps(NewUserResponse(token, all_messages))
                logger.info(f'New User({obj.username}) registered with token: {token}')

                conn.send(response)
                user_join(user)

        elif isinstance(obj, NewMessageRequest):
            if obj.token == user.token:
                logger.info(f'New message from User({user.username}): {obj.message}')
                new_message = Message(user.username, obj.message)
                create_new_job(new_message, user.token)

        else:
            conn.close()
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    logger.info('Server socket started!')

    threading.Thread(target=job_executor, daemon=True).start()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_thread, args=(conn, addr), daemon=True)
        thread.start()


if __name__ == "__main__":
    start_server()
