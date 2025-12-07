from brain_games.engine import run_game
from brain_games.games.brain_prime import DESCRIPTION, question_and_answer


def main():
    run_game(question_and_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
