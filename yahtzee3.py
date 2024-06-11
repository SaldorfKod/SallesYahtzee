from die import Die

# Funktion för att göra ett tärningskast
# Returnera värde 0-6: vilken du fick yahtzee i, eller 0 för förlust
def roll_it():
    # Skapa 5 tärningar (objekt)
    dice = [Die(), Die(), Die(), Die(), Die()]
    # Kasta tärningarna och registrera värden
    for i, d in enumerate(dice):
        d.die_roll()
        # Skriv ut index och värde för varje tärning
        print(f"{i}: {d}")
    # Returnera listan på tärningsobjekt
    return(dice)
    
# Ta emot en lista på tärningsobejkt
def check_yahtzee(pre_rolled_dice):
    #Anta att vi har yahtzee
    yahtzee_flag = True
    # Börja på plats 2 (index 1) och hämför med den innan
    for j in range(1, 5):
        if pre_rolled_dice[j].value != pre_rolled_dice[j-1].value:
            # Om någon av två tärningar inte är samma värde är det ej yahtzee
            yahtzee_flag = False
    # Om det är yahtzee ändras inte flaggan
    if yahtzee_flag == True:
        # Returnera värdet på yahtzeen. Värdet är samma oavsett tärning/index
        return(pre_rolled_dice[1].value)
    else:
        #Om det inte är yahtzee returnera värde 0
        return(0)


# Brasklapp för att inte råka köra annan kod än tänkt, om vi t.ex. 
# vill använda en funktion från programmet någon annanstans
if __name__ == "__main__":
    #0 for no yahtzee or the value of the yahtzee
    yahtzee_value = 0
    # Variabel för att avsluta loop
    keep_it_going = True
    # Vilken tur vi är på
    turn = 0

    print("Welcome to Yahtzee!")
    while keep_it_going == True:
        # +1 till turn så vi inte startar på turn 0
        print(f"Starting turn: {turn+1} of 3, rolling dice")

        #För att se om vi fick yahtzee kallar vi på check:yahtzee...
        #... med listan vi fick som return från rollit
        yahtzee_value = check_yahtzee(roll_it())

        # Om det är yahtzee skriver vi ut det returnerade 
        if yahtzee_value > 0 and yahtzee_value < 7:
            print(f"You got YAHTZEE! in {yahtzee_value}'s")
            # Och avslutar spelet
            print(f"You won! Game over.")
            break

        # Om det inte är yahtzee skriver skriver vi annat meddelande
        if yahtzee_value == 0:
            print(f"Bad luck! :( No yahtzee this time")
            turn += 1

        # Du får bara tre kast
        if turn < 3:
            if input("Want to throw again? (y for yes, anything else for no) ") != "y":
                print(f"Game over. Come again.")
                break

        # Efter tre kast får du välja om du vill köra igen
        if turn > 2:
            if input("Game over! Want to play again? ") == "y":
                turn = 0
            else:
                # Om du inte väljer "y" avslutas spelet
                keep_it_going = not keep_it_going
                break
