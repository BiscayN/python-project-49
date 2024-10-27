from random import randint
from sys import exit
from prompt import string

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_number():
    return randint(1, 100)


def main():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)
    counter = 0
    while counter < 3:
        num = get_number()
        print(f'Question: {num}')
        user_answer = string('Your answer: ')
        if not num % 2:
            if user_answer == 'yes':
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                exit(0)
        else:
            if user_answer == 'no':
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                exit(0)
        counter += 1
    print(f'Congratulations, {name}!')
    exit(0)
