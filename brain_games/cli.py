import prompt


def welcome_user():
    name = ''
    while name == '':
    print('May I have your name? ', end='')
    name = input()
    return name

if __name__ == "__main__":
    welcome_user()
