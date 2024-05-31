"""
The program generates a random 4 digit number.
Try to guess the number in max 10 tries to win.
Rules:
if the digit is in the right position you get R.
if the digit is present in the randomly generated number, but in the wrong position you get Y.
if the digit is not present in the randomly generated number you get B.

EXAMPLE:
Randomly generated number: 1234
Your guess: 1240
Output: RRYB

After each try you will get closer to guessing the number, good luck!
"""

import random

def new_code():
    code = [random.randint(0, 9) for i in range(4)]
    return code

def guess_code(code):
    score = ""
    tries = 0
    while True:
        score = ""
        choice = input("Try to guess the 4 digit number (0-9): ")
        choice = [int(i) for i in choice]
        
        pos = 0
        for _ in choice:
            if choice[pos] == code[pos]:
                score += "R"
            elif choice[pos] in code:
                score += "Y"
            else:
                score += "B"
            pos += 1
        print(f"score: {score}\ntries left: {10 - tries}") 
        tries += 1
        
        if score == "RRRR":
            print("you win!")
            break
        if tries == 10:
            print("you lose..")
            break      
        
code1 = new_code()
guess_code(code1)



