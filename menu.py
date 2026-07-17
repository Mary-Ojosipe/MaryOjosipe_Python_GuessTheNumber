"""
File: menu.py

Purpose:
Handles the main menu and navigation.
It allows the player to start the game, view the
instructions, see the scoreboard, or quit the program.
"""


import scoreboard
from game import play_round, show_instructions, choose_difficulty


def show_main_menu():
    """Print the main menu and return the player's chosen option"""
    print("========================")
    print("   Guess the Number")
    print("========================")
    print("1. Play")
    print("2. Instructions")
    print("3. Scoreboard")
    print("4. Quit")
    return input("Choose an option (1-4): ").strip()


def play_session():
    """Runs the game until the player chooses to stop"""
    choose_difficulty()

    keep_playing = True
    while keep_playing:
        won, attempts_used = play_round()
        scoreboard.record_round(won, attempts_used)

        again = input("Play again? (y/n): ").strip().lower()
        keep_playing = again == "y"


def run():
    """The main menu loop, keeps showing the menu until the play quits"""
    print("Welcome to Guess the Number!\n")

    while True:
        choice = show_main_menu()

        if choice == "1":
            play_session()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            scoreboard.show_scoreboard()
        elif choice == "4":
            print("Thanks for playing!")
            return
        else:
            print("Not a valid option, please try again.")
