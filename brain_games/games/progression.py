from random import randint

QUESTION = 'What number is missing in the progression?'


def get_progression():
    progression = []
    start = randint(1, 20)
    step = randint(1, 5)
    for i in range(10):
        progression.append(start)
        start += step
    prog_str = ' '.join([str(num) for num in progression])
    return prog_str, progression


def conclusion():
    prog_str, progression = get_progression()
    correct_answer = str(progression[randint(0, 9)])
    num_question = prog_str.replace(correct_answer, '..', 1)
    return correct_answer, num_question
