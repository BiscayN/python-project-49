from random import randint
from sys import exit
from prompt import string

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 2:
        return True
    if number == 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)
    counter = 0
    while counter < 3:
        number = randint(0, 100)
        print(f'Question: {number}')
        user_answer = string('Your answer: ')
        if is_prime(number):
            if user_answer == 'yes':
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer "
                      f";(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                exit(0)
        else:
            if not is_prime(number):
                if user_answer == 'no':
                    print('Correct!')
                else:
                    print(f"'{user_answer}' is wrong answer "
                          f";(. Correct answer was 'no'.")
                    print(f"Let's try again, {name}!")
                    exit(0)
        counter += 1
    print(f'Congratulations, {name}!')
    exit(0)
