from random import randint
from math import gcd

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1, num2 = randint(1, 50), randint(1, 50)
    return num1, num2


def conclusion():
    num1, num2 = get_numbers()
    num_question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return correct_answer, num_question
