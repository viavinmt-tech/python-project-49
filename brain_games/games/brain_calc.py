import random

description = 'What is the result of the expression?'
def question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    e = random.choice(['+', '-', '*'])
    match e:
        case '+':
            answer = a + b
        case '-':
            answer = a - b
        case '*':
            answer = a * b
        question = f'{a} {e} {b}'
    return question, str(answer)





