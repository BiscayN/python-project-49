from random import randint
from sys import exit
from prompt import string
from math import gcd

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1, num2 = randint(1, 50), randint(1, 50)
    return num1, num2


def main():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)
    counter = 0
    while counter < 3:
        num1, num2 = get_numbers()
        print(f'Question: {num1} {num2}')
        user_answer = string('Your answer: ')
        if user_answer == str(gcd(num1, num2)):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{gcd(num1, num2)}'.")
            print(f"Let's try again, {name}!")
            exit(0)
        counter += 1
    print(f'Congratulations, {name}!')
    exit(0)
