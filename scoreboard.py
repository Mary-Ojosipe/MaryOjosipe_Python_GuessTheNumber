"""
Keeps track of stats for the whole session.
These are global counters, which live outside of any function.
They keep their value for as long as the program keeps running,
any function in this file can update them.
"""


rounds_played = 0
rounds_won = 0
best_attempts = None                        #fewest attempts taken to win a round so far


def record_round(won, attempts_used):
    """Updates the scoreboard after a round has finished"""
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