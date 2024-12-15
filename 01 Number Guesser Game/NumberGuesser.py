"""
GUESSING GAME WITH PYTHON:
    CREATE A GAME WITH PYTHON WHERE USER INPUTS A NUMBER BETWEEN 1 AND 99
    AND HAS TO GUESS THE SAME NUMBER AS RANDOM NUM GENERATOR USING RANDINT?

    1. TAKE USER INPUT NUMBER
    2. GENERATE NUM BETWEEN 1 AND 99
    3. OUTPUT:
                CORRECT / INCORRECT 
                YOUR GUESS:
                ACTUAL NUMBER:
USED WHILE TRUE TO INFINITLY ITERATE OVER CODE SO USER CAN GUESS FOR AS LONG AS THEY WISH

CODE COULD BE POTENTIALLY CHANGED TO GIVE USER 10 TRIES (MORE OR LESS) TO GUESS. A COUNTER COULD BE USED TO COUNT HOW
MANY USER HAS GUESSED OUT OF 10



NOTES
======
LAST PRINT FUNCTION INCORRECTLY OUTPUTTING: You correctly guessed: 0 and incorrectly guessed: 1 out of 10!
"""
import random

correctCount = 0
incorrectCount = 0
randomNum = random.randint(1, 10)

for i in range(10, 0, -1):
    guessNum = int(input("Please enter a number between 1 & 10: "))

    if guessNum == randomNum:
        print("Correct!", "\nYou guessed:", guessNum, "and the actual number was:", randomNum,".")
        i -= 1
        print(i, "Tries remaining", "\n")
        correctCount += 1
        
    elif guessNum != randomNum:
        print("Incorrect!", "\nYou guessed: ", guessNum, "and the actual number was: ", randomNum, ".")
        i -= 1
        print(i, "Tries remaining", "\n\n")
        incorrectCount += 1
        
if i == 0:
    print("GAME OVER :(")

print("You correctly guessed:",  correctCount, "and incorrectly guessed:", incorrectCount, "out of 10!")
