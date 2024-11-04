from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_number():
    return randint(1, 100)


def conclusion():
    num_question = get_number()
    if is_even(num_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num_question
