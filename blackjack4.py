
user_points = 0
comp_points = 0

def main():
    global user_points
    global comp_points

    print (f"User points: {user_points}")
    print (f"Computer points: {comp_points}")
    
    global score
    import random
  
    c1 = random.randint(2, 11)
    c2 = random.randint(2, 11)
    c3 = random.randint(2, 11)
    c4 = random.randint(2, 11)

    co1 = random.randint(2, 11)
    co2 = random.randint(2, 11)
    co3 = random.randint(2, 11)
    co4 = random.randint(2, 11)
    

    def draw():
        global user_points
        global comp_points
        global score
        print ("Your third card is " + str(c3))
        score = c1 + c2 + c3
        print ("You have a total of " + str(score) + " points")
        if score == 21:
            print ("Blackjack! You win")
            user_points += 1
            play_again()

        elif score > 21:
            print ("Strike! You lose")
            comp_points += 1
            play_again()
        
        

    def draw2():
        global user_points
        global comp_points
        global score
        print ("Your fourth card is " + str(c4))
        score = c1 + c2 + c3 + c4
        print ("You have a total of " + str(score) + " points")
        if score == 21:
            print ("Blackjack! You win")
            user_points += 1
            play_again()
        elif score > 21:
            print ("Strike! You lose")
            comp_points += 1
            play_again()
        
        
    def play_again():
        while True:
            play = input("Do you want to play again? y/n: ").lower()
            if play == "y":
                main()
            elif play == "n":
                print ("Bye")
                quit()
            else:
                print ("Type a valid answer. y/n")
                continue

    def final_score():
        global user_points
        global comp_points
        global score
        print ("Your final score is: " + str(score))
        print ("Computer final score is: " + str(c_score))
        if score == c_score:
            print ("It's a tie")
        elif score < c_score:
            print ("You lost :( ")
            comp_points += 1
        else:
            print ("You win!")
            user_points += 1
        play_again()
        

    def comp():
        print ("Computer draws 2 cards. first card is " + str(co1) + ". Second card is hidden")

    def comp2():
        global user_points
        global comp_points
        global c_score
        print ("Computer first 2 cards are: " + str(co1) + " and " + str(co2))
        c_score = co1 + co2
        print ("Computer has " + str(c_score) + " points")
        if c_score == 21:
            print ("Blackjack, computer wins")
            comp_points += 1
        elif c_score < 15:
            print ("Computer draws one more card. The card is: " + str(co3))
            c_score = co1 + co2 + co3
            print ("Computer has " + str(c_score) + " points")
            if c_score == 21:
                print ("Blackjack, computer wins")
                comp_points += 1
            elif c_score > 21:
                print ("Strike for computer, You win!")
                user_points += 1
                play_again()
            elif c_score < 15:
                print ("Computer draws one more card. The card is: " + str(co4))
                c_score = co1 + co2 + co3 + co4
                print ("Computer has " + str(c_score) + " points")
                if c_score == 21:
                    print ("Blackjack, computer wins")
                    comp_points += 1
                elif c_score > 21:
                    print ("Strike for computer, You win!")
                    user_points += 1
                    play_again()
                else:
                    print ("Computer stops.")
        else:
            print ("Computer stops.")
    

    print ("Welcome to blackjack!")

    comp ()

    print ("Your first 2 cards are: " + str(c1) + " and " + str(c2))
    score = c1 + c2

    if score == 21:
        print ("Blackjack! You win")
        user_points += 1
        play_again()
    else:
        pass

    print ("You have a total of " + str(score) + " points")

    

    while True:
        choice1 = input("press 'q' to draw a card or 'e' to stop: ").lower()
    
        if choice1 == "q":
            draw()
            
        elif choice1 == "e":
            comp2()
            final_score()
            
        else:
            print ("Choose a valid option: q/e")
            continue

        while True:
            choice2 = input("press 'q' to draw a card or 'e' to stop: ").lower()
            if choice2 == "q":
                draw2()
                print ("4 cards is the maximum ammount.")
                comp2()
                final_score()
            elif choice2 == "e":   
                comp2()
                final_score()
            else:
               print ("Choose a valid option: q/e")
            continue



main()

    

