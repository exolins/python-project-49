import random


def question_calc():
    operaion = random.randint(0, 2)
    a = random.randint(0, 50)
    b = random.randint(0, 50)

    match operaion:
        case 0:
            answer = str(a + b)
            question = f'{str(a)} + {str(b)}'
        case 1:
            answer = str(a - b)
            question = f'{str(a)} - {str(b)}'
        case 2:
            answer = str(a * b)
            question = f'{str(a)} * {str(b)}'
    return (question, answer)

    
