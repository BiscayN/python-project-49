from prompt import string
from sys import exit


def welcome():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def source(correct_answer, num_question, user_name):
    print(f'Question: {num_question}')
    user_answer = string('Your answer: ')
    if correct_answer == user_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer "
              f";(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        exit(0)


def solution(game):
    user_name = welcome()
    print(game.QUESTION)
    rounds_counter = 0
    while rounds_counter < 3:
        correct_answer, num_question = game.conclusion()
        source(correct_answer, num_question, user_name)
        rounds_counter += 1
    print(f'Congratulations, {user_name}!')
    exit(0)
