import random
from cli import welcome_user

def is_even():
    count = 0
    d = welcome_user
    while count < 3:
        a = random.randint(1, 100)
        print(f'Question: {a}')
        c = input('Your answer:')
        if a % 2 == 0:
            b = 'yes'
        else:
            b = 'no'
        if b == c:
            print('Correct!')
            count +=1
        else: 
            print(f"'{c}' is wrong answer ;(. Correct answer was '{b}'\nLet's try again, {d}!")
            break
    print(f'Congratulations, {d}!')

