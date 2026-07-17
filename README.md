# Guess the Number

A number-guessing game with a main menu, difficulty levels, direction hints, tiered proximity hints, and a session scoreboard, built as my First Python Project submission.

See 'flowchart' for the game-logic flowchart

---

# How to run

No external libraries needed, just Python 3 and its built-in 'random' module.

'''bash
python3 main.py
'''

---

# How to play

1. From the main menu, choose **1** to play
2. Pick a difficulty: **Easy**, **Medium**, or **Hard**
3. Guess the random number within your attempt limit
4. After each incorrect guess, you get two hint:
    - **Direction:** Too Low or Too High
    - **Proximity:** Way Off, Off, Close, Very Close, Almost There
        (the closer your guess, the more specific the hint)
5. After each round you can choose to play again at the same difficulty, or return to the main menu.

# Difficulty levels

|
Difficulty
|
Range
|
Attempts
|
|
---
|
---
|
---
|
|
Easy
|
1-50
|
10
|
|
Medium
|
1-100
|
8
|
|
Hard
|
1-250
|
7
|

---

# Features
