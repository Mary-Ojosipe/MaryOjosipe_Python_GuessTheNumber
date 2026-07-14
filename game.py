"""
This file holds the actual game logic.
Currently just picks a random number and takes a guess.
"""


import random
from settings import MIN_NUMBER, MAX_NUMBER

def play_round():
    # picks a random number in the range
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # asks player for a guess
    guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))

    print(f"You guessed: {guess}")
    print(f"The secret number was: {secret_number}")