import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    x = random.randint(1, 50)  # NOSONAR
    question = f'{x}'
    if x == 2:
        answer = 'yes'
        return question, answer
    if x == 1:
        answer = 'no'
        return question, answer
    count = 0
    a = 1
    while x > a:
        if x % a == 0:
            count += 1
            x = x / a
        a += 1
        if x == 2:
            count += 1
    if count >= 2:
        answer = 'no'
        return question, answer
    else:
        answer = 'yes'
        return question, answer



