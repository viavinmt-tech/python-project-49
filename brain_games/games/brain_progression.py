import random

DESCRIPTION = 'What number is missing in the progression?'


def progression(a, index, step):
    progression = []
    for i in range(10):
        a = a + index * step
        progression.append(a)
    return progression


def question_and_answer():
    a = random.randint(1, 50)  # NOSONAR
    index = random.randint(0, 9)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    p = progression(a, index, step) 
    answer = p[index]
    p_ind = p.copy()
    p_ind[index] = '..'
    p_ind = map(str, p_ind)
    question = f"{' '.join(p_ind)}"
    return question, str(answer)
