import random

# prime


def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def question_prime():
    answer = ""
    number_guess = random.randint(1, 100)
    if is_prime(number_guess):
        answer = "yes"
    else:
        answer = "no"
    return (number_guess, answer)
