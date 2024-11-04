from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 2:
        return True
    for i in range(2, int(number ** 0.5) + 2):
        if number % i == 0:
            return False
    return True


def get_values():
    return randint(2, 100)


def conclusion():
    num_question = get_values()
    if is_prime(num_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num_question
