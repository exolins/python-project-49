import random

# gcd


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def question_gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = get_gcd(a, b)
    return (f"{str(a)} {str(b)}", str(answer))
