# ЗАПУСКАТИ КОД ЛИШЕ У ТЕРМІНАЛІ А НЕ У JUPYTER
# ІНАКШЕ ТЕКСТ МОЖЕ ВІДОБРАЖАТИСЬ НЕКОРЕКТНО

import time
from config import config

level = 0
answers_map = []


def delay_print(s):
    for c in s:
        print(c, end='')
        time.sleep(0.05)
    print()


def error_or_continue(status):
    if not status:
        delay_print('\n Неіснуюча відповідь на питання !!')
        exit(1)


def submit_user_answer(answer, index):
    for a in config[level][index]['answers']:
        if a['answer'] == answer or a['answer'] == 'RANDOM':
            delay_print('\n' + a['text'])

            answers_map.append(a['answer_id'])
            return True

    return False


delay_print(config[level][0]['question'])
game_status = submit_user_answer(input(': '), 0)

error_or_continue(game_status)
level += 1

while True:

    selected_question = None
    question_index = None
    for i, v in enumerate(config[level]):
        if answers_map[level - 1] in v['require']:
            selected_question = v
            question_index = i
            break
    if selected_question is None or question_index is None:
        exit(0)

    delay_print(selected_question['question'])

    if len(selected_question['answers']) == 0:
        exit(0)

    game_status = submit_user_answer(input(': '), question_index)

    error_or_continue(game_status)
    level += 1

    if len(config) == level:
        print(answers_map)
        exit(0)
