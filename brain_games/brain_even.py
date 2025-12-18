import random


def is_even(number):
    return number % 2 != 1


def question_even():
    answer = ''
    number_guess = random.randint(1, 100)
    if is_even(number_guess):
        answer = 'yes'
    else:
        answer = 'no'
    return (number_guess, answer)
    

