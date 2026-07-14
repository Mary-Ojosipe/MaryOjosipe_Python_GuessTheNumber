"""
This file holds the actual game logic.
"""


import random
from settings import (MIN_NUMBER, MAX_NUMBER, MAX_ATTEMPTS,
                      ALMOST_THERE_DISTANCE, VERY_CLOSE_DISTANCE,
                      CLOSE_DISTANCE, OFF_DISTANCE)

def get_valid_guess():
    """
    Asks player for a guess till they type a valid whole number.
    A bad guess (like letters) doesn't use up an attempts.
    """
    while True:
        guess_text = input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: ")
        try:
            return int(guess_text)
        except ValueError:
            print("That's not a whole number, please try again.")


def get_proximity_hint(distance):
    """
    Let's you know how far off a guess was.
    Smaller distance means the guess was closer to the secret number.
    """
    if distance <= ALMOST_THERE_DISTANCE:
        return "Almost There"
    elif distance <= VERY_CLOSE_DISTANCE:
            return "Very Close"
    elif distance <= CLOSE_DISTANCE:
        return "Close"
    elif distance <= OFF_DISTANCE:
        return "Off"
    else:
        return "Way Off"


def play_round():
    # picks a random number in the range
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_used = 0

    while attempts_used < MAX_ATTEMPTS:
        guess = get_valid_guess()
        attempts_used += 1

        if guess == secret_number:
            print(f"Correct! You got it in {attempts_used} attempts.")
            return True, attempts_used
        
        distance = abs(guess - secret_number)
        hint = get_proximity_hint(distance)
        
        if guess < secret_number:
            print(f"Too Low, {hint}")
        else:
            print(f"Too High, {hint}")

        print(f"Attempts left: {MAX_ATTEMPTS - attempts_used}")
    
    print(f"Out of attempts! The number was {secret_number}.")
    return False, attempts_used