from brain_games.engine import run_game
from brain_games.games.brain_progression import question_and_answer, description

def main():
    run_game(question_and_answer, description)

if __name__ == "__main__":
    main()

