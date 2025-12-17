import prompt

from brain_games.brain_even import brain_even


def main():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    brain_even()
    print(f'Congratulations, {name}!')


