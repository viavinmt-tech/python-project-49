def run_game(question_and_answer, description):
    from brain_games.cli import welcome_user
    
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}')
    
    print(description)

    count = 0
    need_count = 3

    while count < need_count: 
        question, answer = question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count +=1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')
    

