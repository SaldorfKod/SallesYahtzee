from die import Die

#separat funktion för att rulla 5 tärningar
#return värde 0-6: vilken du fick yahtzee i eller 0 för förlust
def roll_it():
    #define 5 dice
    dice = [Die(), Die(), Die(), Die(), Die()]
    #set the value of each die as the result of a roll
    for i, d in enumerate(dice):
        d.die_roll()
        #print the index and value of each die
        print(f"{i}: {d}")
    #return the list of the dice
    return(dice)
    
#Accept a list of 5 dice
def check_yahtzee(pre_rolled_dice):
    #Assume we have yahtzee
    yahtzee_flag = True
    #Start at index 1, compare to previous
    for j in range(1, 5):
        if pre_rolled_dice[j].value != pre_rolled_dice[j-1].value:
            #If they are not the same it is not yahtzee
            yahtzee_flag = False
    #If the were all the same, flag is still true
    if yahtzee_flag == True:
        #Return the value of the yahtzee. Index does not matter
        return(pre_rolled_dice[1].value)
    else:
        #A return value of 0 will indcate no yahtzee
        return(0)



if __name__ == "__main__":
    #0 for no yahtzee or the value of the yahtzee
    yahtzee_value = 0
    #We will change this to quit the game
    keep_it_going = True
    #The turn we are on
    turn = 0
    print("Welcome to Yahtzee!")
    while keep_it_going == True:
        #+1 to turn since we start at 0
        print(f"Starting turn: {turn+1} of 3, rolling dice")
        #To check if we have yahtzee we call the check_yahtzee function..
        #..with the list returned by the roll_it function
        yahtzee_value = check_yahtzee(roll_it())
        #With returned value we can print what value we got yahtzee in
        if yahtzee_value > 0 and yahtzee_value < 7:
            print(f"You got YAHTZEE! in {yahtzee_value}'s")
            print(f"You won! Game over.")
            break
        #With 0 as return value we can easily print a lose message
        if yahtzee_value == 0:
            print(f"Bad luck! :( No yahtzee this time")
            turn += 1
        #You are only allowed 3 tries
        if turn < 3:
            if input("Want to throw again? (y for yes, anything else for no) ") != "y":
                print(f"Game over. Come again.")
                break
        if turn > 2:
            #User can restart the game if they like to
            if input("Game over! Want to play again? ") == "y":
                turn = 0
            else:
                #Else we will quit the game
                keep_it_going = not keep_it_going
                break
