import prompt


def question_show(question):
    print(f'Question: {question}')


def answer_prompt():
    return prompt.string('Your answer: ')


def round_win_show():
    print('Correct!')


def hello_user(user_name):
    print(f"Hello, {user_name}")


def round_lost_show(answer_user, answer_right, user_name):
    print(f"'{answer_user}' is wrong answer ;(.", end='')
    print(f"Correct answer was '{answer_right}'")
    print(f"Let's try anain, {user_name}!")


def game_win_show(user_name):
    print(f"Congratulations, {user_name}")


def game_welcome_show(game_name):
    match game_name:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
        case 'progression':
            print('What number missing in the progression?')
        case 'prime':
            print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prompt_user_name():
    return prompt.string('May I have your name? ')


def welcome_to_brain_games():
    print('Welcome to the Brain Games')
