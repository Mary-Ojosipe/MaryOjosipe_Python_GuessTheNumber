"""
File: scoreboard.py

Purpose:
Keeps track of the player's statistics for the current session.
It records games played, games won, win percentage, and the best winning score.
"""


rounds_played = 0
rounds_won = 0
best_attempts = None            # lowest number of guesses needed to win a round


def record_round(won, attempts_used):
    """Updates the session statistics after each completed round"""
    global rounds_played, rounds_won, best_attempts

    rounds_played += 1

    if won:
        rounds_won += 1
        if best_attempts is None or attempts_used < best_attempts:
            best_attempts = attempts_used


def show_scoreboard():
    """Displays the current session stats."""
    win_percent = (rounds_won / rounds_played * 100) if rounds_played else 0

    print("\n--- Scoreboard ---")
    print(f"Rounds played: {rounds_played}")
    print(f"Rounds won: {rounds_won}")
    print(f"Win percentage: {win_percent:.1f}%")
    if best_attempts is not None:
        print(f"Best round: {best_attempts} attempts")
    else:
        print("Best round: no wins yet")
    print("--------------------------\n")
