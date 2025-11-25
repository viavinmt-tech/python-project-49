from brain_games.cli import welcome_user
from brain_even import


def main():

    print('Welcome to the Brain Games!')
    welcome_user()
    name = welcome_user()
    print(f'Hello, {name}')
    is_even()


if __name__ == "__main__":
    main()

