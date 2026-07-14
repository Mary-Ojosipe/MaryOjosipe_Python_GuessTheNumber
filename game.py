"""
This file holds the actual game logic.
"""


import random
from settings import MIN_NUMBER, MAX_NUMBER, MAX_ATTEMPTS

def get_valid_guess():
    """
    Asks player for a guess till they type a valid whole number.
    A bad guess (like letters) doesn't use up on of their attempts.
    """
    while True:
        guess_text = input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: ")
        try:
            return int(guess_text)
        except ValueError:
            print("That's not a whole number, please try again.")


def play_round():
    # picks a random number in the range
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_used = 0

    while attempts_used < MAX_ATTEMPTS:
        guess = get_valid_guess()
        attempts_used += 1

        if guess == secret_number:
            print(f"Correct! You got it in {attempts_used} attempts.")
            return
        
        if guess < secret_number:
            print("Too Low")
        else:
            print("Too High")

        print(f"Attempts left: {MAX_ATTEMPTS - attempts_used}")
    print(f"Out of attempts! The number was {secret_number}.")