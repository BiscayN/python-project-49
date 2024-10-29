from random import randint
from random import choice
from sys import exit
from prompt import string

START_QUESTION = 'What is the result of the expression?'


def get_values():
    num1, num2 = randint(1, 50), randint(1, 50)
    operator = choice(['+', '-', '*'])
    return num1, num2, operator


def main():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(START_QUESTION)
    counter = 0
    while counter < 3:
        num1, num2, operator = get_values()
        question = f'{max(num1, num2)} {operator} {min(num1, num2)}'
        print(f'Question: {max(num1, num2)} {operator} {min(num1, num2)}')
        user_answer = string('Your answer: ')
        if str(eval(question)) == str(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{eval(question)}'")
            print(f"Let's try again, {name}!")
            exit(0)
        counter += 1
    print(f'Congratulations, {name}!')
    exit(0)
