from die import Die

#separat funktion för att rulla 5 tärningar
#return värde 0-6: vilken du fick yahtzee i eller 0 för förlust
def rollIt():
    dice = [Die(), Die(), Die(), Die(), Die()]
    for i, d in enumerate(dice):
        d.DieRoll()
        #d.value = 5  # Test if yahtzee works
        print(f"{i}: {d}")
        #Nu har vi rullat fem tärningar och printat värdet av dem

    # YAHTZEE
    #anta att vi har yahtzee
    yahFlag = True
    for j in range(1, 5):
        #Börja på index 1 (den andra) och jmf med den innan om de samma
        if dice[j].value != dice[j-1].value:
            # Om inte samma: det är inte yahtzee
            yahFlag = False
    #om alla var samma är flaggan ff true
    if yahFlag == True:
        #Istället för print, return value av yahtzee. print i main.
        #När yahtzee, är alla samma värde så kan använda vilken som
        return(dice[1].value)
    else:
        #Annars return 0 för förlust
        return(0)



def main():
    yahValue = 0
    keepItGoing = True
    intTurn = 0
    print("Welcome to Yahtzee!")
    while keepItGoing == True:
    # while intTurn < 3:
        print(f"Starting turn: {intTurn+1} of 3, rolling dice")
        yahValue = int(rollIt())
        if yahValue > 0 and yahValue < 7:
            print(f"You got YAHTZEE! in {yahValue}'s")
            print(f"You won! Game over.")
            break
        if yahValue == 0:
            print(f"Bad luck! :( No yahtzee this time")
            intTurn += 1
        if intTurn < 3:
            if input("Want to throw again? (y for yes, anything else for no) ") != "y":
                print(f"Game over. Come again.")
                break
        if intTurn > 2:
            if input("Game over! Want to play again? ") == "y":
                intTurn = 0
            else:
                keepItGoing = not keepItGoing
                break


    #YahtzeeMainClass()

if __name__ == '__main__':
    main()