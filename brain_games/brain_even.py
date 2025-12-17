import random

import prompt


def is_even(number):
    if number % 2 == 1:
        return 'no'
    return 'yes'


def brain_even():
    count = 0
    while count < 3:
        number_guess = random.randint(1, 100)
        print(f'Question: {number_guess}')
        answer = prompt.string('Your answer: ')
        answer_correct = is_even(number_guess)
        if answer != answer_correct:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{answer_correct}'")
            count = 0
            continue
        print('Correct!')
        count += 1
