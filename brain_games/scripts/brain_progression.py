from random import randint
from sys import exit
from prompt import string

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


def main():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)
    counter = 0
    while counter < 3:
        prog_str, progression = get_progression()
        answer = progression[randint(0, 9)]
        changed_progression = prog_str.replace(str(answer), '..', 1)
        print(f'Question: {changed_progression}')
        user_answer = string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            exit(0)
        counter += 1
    print(f'Congratulations, {name}!')
    exit(0)
