from die import Die

#separat funktion för att rulla 5 tärningar
#return värde 0-6: vilken du fick yahtzee i eller 0 för förlust
def rollIt():
    #define 5 dice
    dice = [Die(), Die(), Die(), Die(), Die()]
    #set the value of each die as the result of a roll
    for i, d in enumerate(dice):
        d.DieRoll()
        #print the index and value of each die
        print(f"{i}: {d}")
    #return the list of the dice
    return(dice)
    
#Accept a list of 5 dice
def checkYahtzee(preRolledDice):
    #Assume we have yahtzee
    yahFlag = True
    #Start at index 1, compare to previous
    for j in range(1, 5):
        if preRolledDice[j].value != preRolledDice[j-1].value:
            #If they are not the same it is not yahtzee
            yahFlag = False
    #If the were all the same, flag is still true
    if yahFlag == True:
        #Return the value of the yahtzee. Index does not matter
        return(preRolledDice[1].value)
    else:
        #A return value of 0 will indcate no yahtzee
        return(0)



def main():
    #Do we have yahtzee yes/no
    yahValue = 0
    #We will change this to quit the game
    keepItGoing = True
    #The turn we are on
    intTurn = 0
    print("Welcome to Yahtzee!")
    while keepItGoing == True:
        #+1 to turn since we start at 0
        print(f"Starting turn: {intTurn+1} of 3, rolling dice")
        #To check if we have yahtzee we call the checkYahtzee function..
        #..with the list returned by the rollIt function
        yahValue = checkYahtzee(rollIt())
        #With returned value we can print what value we got yahtzee in
        if yahValue > 0 and yahValue < 7:
            print(f"You got YAHTZEE! in {yahValue}'s")
            print(f"You won! Game over.")
            break
        #With 0 as return value we can easily print a lose message
        if yahValue == 0:
            print(f"Bad luck! :( No yahtzee this time")
            intTurn += 1
        #You are only allowed 3 tries
        if intTurn < 3:
            if input("Want to throw again? (y for yes, anything else for no) ") != "y":
                print(f"Game over. Come again.")
                break
        if intTurn > 2:
            #User can restart the game if they like to
            if input("Game over! Want to play again? ") == "y":
                intTurn = 0
            else:
                #Else we will quit the game
                keepItGoing = not keepItGoing
                break


    #YahtzeeMainClass()

if __name__ == '__main__':
    main()
