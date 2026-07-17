"""
File: game.py

Purpose:
Contains the main game logic.
It runs each round, checks the player's guesses,
and gives hints until the round ends.
"""


import random
import settings

# icons shown next to each proximity hint
PROXIMITY_ICONS = {
    "Way Off": "🧊",
    "Off": "❄️",
    "Close": "☀️",
    "Very Close": "🔥",
    "Almost There": "🔥🔥",
}


def show_instructions():
    """Shows the rules, available any time from the main menu"""
    print("========================")
    print("   Guess the Number")
    print("========================")
    print(f"Difficulty: {settings.current_difficulty}")
    print(f"I'm thinking of a number between {settings.current_min} and {settings.current_max}.")
    print(f"You have {settings.current_attempts} attempts to guess it.")
    print("After each guess, you'll receive two hint:")
    print(" - Direction: 'Too Low' or 'Too High'")
    print(" - Proximity: 'Way Off' or 'Off' or 'Close' or 'Very Close' or 'Almost There'")
    print("Good luck!\n")


def choose_difficulty():
    """Asks the player to pick a difficulty before a round starts"""
    print("Choose a difficulty: Easy / Medium / Hard")
    while True:
        choice = input("> ").strip().title()
        if choice in settings.DIFFICULTIES:
            settings.set_difficulty(choice)
            return
        print("Not a valid difficulty, please type Easy, Medium, or Hard")


def get_valid_guess():
    """
    Keeps asking until the player enters a valid whole number.
    Invalid inputs do not count as an attempt.
    """
    while True:
        guess_text = input(f"Guess a number between {settings.current_min} and {settings.current_max}: ")
        try:
            return int(guess_text)
        except ValueError:
            print("That's not a valid number, please try again.")


def get_proximity_hint(distance):
    """
    Tells the player how close their guess is.
    A smaller distance means the guess is closer to the number.
    """
    if distance <= settings.ALMOST_THERE_DISTANCE:
        return "Almost There"
    elif distance <= settings.VERY_CLOSE_DISTANCE:
            return "Very Close"
    elif distance <= settings.CLOSE_DISTANCE:
        return "Close"
    elif distance <= settings.OFF_DISTANCE:
        return "Off"
    else:
        return "Way Off"


def play_round():
    """
    Plays a full round of the game using the current settings.
    Returns (won, attempts_used) so the scoreboard can be updated.
    """
    # chooses a random number for this round
    secret_number = random.randint(settings.current_min, settings.current_max)
    attempts_used = 0

    print("========================")
    print("   Guess the Number")
    print("=======================\n")

    while attempts_used < settings.current_attempts:
        print(f"Attempts Left: {settings.current_attempts - attempts_used}")
        guess = get_valid_guess()
        attempts_used += 1
        print(f"Guess: {guess}")

        if guess == secret_number:
            print(f"Correct! You got it in {attempts_used} attempts.\n")
            return True, attempts_used
        
        distance = abs(guess - secret_number)
        hint = get_proximity_hint(distance)
        direction = "Too High" if guess > secret_number else "Too Low"
        icon = PROXIMITY_ICONS[hint]

        print(direction)
        print(f"{icon} {hint}\n")
    
    print(f"Out of attempts! The number was {secret_number}.\n")
    return False, attempts_used
