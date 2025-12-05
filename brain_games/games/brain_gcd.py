import random

description = 'Find the greatest common divisor of given numbers.'
def question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    while b != 0:
        a,b= b, a % b
    question = f'{a} {b}'
    if b == 0:
        answer = a 
    return question, str(answer)
