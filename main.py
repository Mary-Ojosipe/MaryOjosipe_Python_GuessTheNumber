"""
This is the file you run to start the game.
It asks the player if they want to play another round.
Shows the scoreboard after every round.
"""


from game import play_round
from scoreboard import record_round, show_scoreboard

def main():
    keep_playing = True
    while keep_playing:
        won, attempts_used = play_round()
        record_round(won, attempts_used)
        show_scoreboard()
        
        #play_round()
        again = input("Play again? (y/n): ").strip().lower()
        keep_playing = again == "y"
    print("Thanks for playing!")

if __name__ == "__main__":
    main()