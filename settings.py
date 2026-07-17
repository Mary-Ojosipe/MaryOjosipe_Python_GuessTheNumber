"""
File: settings.py

Purpose:
Stores the game settings and difficulty presets.
Changing values here updates the settings used throughout the game.
"""

DIFFICULTIES = {
    "Easy": {"min": 1, "max": 50, "attempts": 10},
    "Medium":   {"min": 1, "max": 100, "attempts": 8},
    "Hard": {"min": 1, "max": 250, "attempts": 7},
}


# distance ranges used to decide which hint to show
# smaller the distance, the closer the guess
ALMOST_THERE_DISTANCE = 2
VERY_CLOSE_DISTANCE = 5
CLOSE_DISTANCE = 10
OFF_DISTANCE = 20


# stores the currently selected difficulty
# these global values are shared across the program
current_difficulty = "Medium"
current_min = DIFFICULTIES[current_difficulty]["min"]
current_max = DIFFICULTIES[current_difficulty]["max"]
current_attempts = DIFFICULTIES[current_difficulty]["attempts"]


def set_difficulty(name):
    """Switch to one of the difficulty presets (Easy / Medium / Hard)"""
    global current_difficulty, current_min, current_max, current_attempts
    preset = DIFFICULTIES[name]
    current_difficulty = name
    current_min = preset["min"]
    current_max = preset["max"]
    current_attempts = preset["attempts"]
