
from die import Die

class YahtzeeMainClass:
    def __init__(self):
        #ändra ds till dies för tydlighet
        self.dies = [Die(), Die(), Die(), Die(), Die()]
        self.keepItGoing = True
        
        while self.keepItGoing == True:
            intTurn = 0
            
            print("Welcome to Yahtzee!")
            
            while intTurn < 3:
                print(f"Starting turn: {intTurn+1} of 3, rolling dice")
                for i, d in enumerate(self.dies):
                    d.DieRoll()
                    # d.value = 5  # Test if yahtzee works
                    print(f"{i}: {d}")
                # YAHTZEE
                flag = True
                for j in range(1, 5):
                    if self.dies[j].value != self.dies[j-1].value:
                        # Set flag to false
                        flag = False
                if flag == True:
                    print(f"You got YAHTZEE! in {self.dies[0].value}'s")
                    return
                else:
                    # Here we check if there is no Yahtzee: then we check what turn we are on and ask the player if we want to continue or not
                    if intTurn != 2:
                        if input("Want to throw again? (y for yes, anything else for no) ") == "y":
                            intTurn += 1
                        else:
                            self.keepItGoing = not self.keepItGoing
                            break
                    else:
                        if input("Game over! Want to play again? ") == "y":
                            intTurn = 0
                        else:
                            self.keepItGoing = not self.keepItGoing
                            break
#separat funktion för att rulla 5 tärningar
#return värde 0-6: vilken du fick yahtzee i eller 0 för förlust
def rollIt():
    dies = [Die(), Die(), Die(), Die(), Die()]
    for i, d in enumerate(dies):
        d.DieRoll()
        # d.value = 5  # Test if yahtzee works
        print(f"{i}: {d}")
        #Nu har vi rullat fem tärningar och printat värdet av dem

    # YAHTZEE
    yahFlag = True
    for j in range(1, 5):
        #dubbelkolla att .value fungerar som tänkt här
        #Börja på index 1 (den andra) och jmf med den innan om de samma
        if dies[j].value != dies[j-1].value:
            # Om inte samma: det är inte yahtzee
            yahFlag = False
        if yahFlag == True:
            #print(f"You got YAHTZEE! in {self.ds[0].value}'s")
            #Istället för print, return value av yahtzee. print i main.
            return(dies[1].value)
        else:
            #Annars return 0 för förlust
            return(0)



def main():
    yahValue = 0
    keepItGoing = True
    while keepItGoing == True:
        intTurn = 0
        print("Welcome to Yahtzee!")
        while intTurn < 3:
            print(f"Starting turn: {intTurn+1} of 3, rolling dice")
            yahValue = int(rollIt())
            if yahValue > 0:
                print(f"You got YAHTZEE! in {yahValue}'s")
            if yahValue == 0:
                print(f"Bad luck! :(")
                if intTurn < 2:
                    if input("Want to throw again? (y for yes, anything else for no) ") == "y":
                            intTurn += 1
                else:
                    keepItGoing = not keepItGoing
                    break


    #YahtzeeMainClass()

if __name__ == '__main__':
    main()