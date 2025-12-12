import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    a = random.randint(1, 100) # NOSONAR
    question = f'{a}'
    if a % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer



