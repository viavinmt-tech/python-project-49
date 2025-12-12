import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    a = random.randint(1, 100)# NOSONAR
    b = random.randint(1, 100)# NOSONAR
    question = f'{a} {b}'
    while b != 0:
        a, b = b, a % b
    if b == 0:
        answer = a 
    return question, str(answer)
