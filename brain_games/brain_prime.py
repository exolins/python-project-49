import random
#prime

def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True




def question_prime():
    answer = ''
    number_guess = random.randint(1, 100)
    if is_prime(number_guess):
        answer = 'yes'
    else:
        answer = 'no'
    return (number_guess, answer)
    

