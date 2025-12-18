import random


# progression
def question_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    count = random.randint(5, 10)
    miss = random.randint(0, count)
    question = ()
    answer = 0

    for index in range(count):
        current_element = start + index * step
        if index == miss:
            question = (*question, "..")
            answer = str(current_element)
        else:
            question = (*question, str(current_element))
    return (" ".join(question), answer)
