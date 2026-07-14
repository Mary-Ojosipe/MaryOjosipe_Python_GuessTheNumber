"""
This is the file you run to start the game.
"""


from game import play_round

def main():
    keep_playing = True
    while keep_playing:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        keep_playing = again == "y"
    print("Thanks for playing!")

if __name__ == "__main__":
    main()