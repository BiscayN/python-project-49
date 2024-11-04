from random import randint
from random import choice

QUESTION = 'What is the result of the expression?'


def get_values():
    num1, num2 = randint(1, 50), randint(1, 50)
    operator = choice(['+', '-', '*'])
    return num1, num2, operator


def conclusion():
    num1, num2, operator = get_values()
    num_question = f'{max(num1, num2)} {operator} {min(num1, num2)}'
    correct_answer = str(eval(num_question))
    return correct_answer, num_question
