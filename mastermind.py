import random

def new_code():
    code = [random.randint(0, 9) for i in range(4)]
    return code

def guess_code(code):
    score = ""
    tries = 0
    while True:
        score = ""
        choice = input("enter 4 digit number (0-9): ")
        choice = [int(i) for i in choice]
        
        pos = 0
        for num in choice:
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
print(code1)
guess_code(code1)



