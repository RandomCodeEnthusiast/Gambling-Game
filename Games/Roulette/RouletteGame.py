def Roulette_Game(Player : int) -> tuple :

    #Imports
    from random import choice
    from GeneralSetup import BetAmountSetup
    from GeneralSetup import BetTypeSetup

    #SETUP : user input 

    #Done in a loop to account for input errors
    for i in range (3) : 

        #Asking the type (color,number,even,high,etc...), and the amount of the bet
        BetAmount=BetAmountSetup(Player)
        BetType=BetTypeSetup()
        successful=True

        #Setting default values for bet color and number
        BetColor="None"
        BetNumber=[42] #Arbitrary number that won't appear on the roulette

        #Determining what the bet is and asking further questions if necessary
        if BetType=="color" : 
            BetColor=input("Bet Color : ").lower()
            Multiplier=2

        elif "number" in BetType: 
            print("Please input numbers beetween 0 and 36, otherwise you will not gain anything")
            BetNumber=[int(x) for x in input("Bet Number(s) : ").split()]
            Multiplier=36/len(BetNumber) 

        #NOTE : This isn't the the Split or Square BetType because numbers aren't adjacent : those aren't implemented

        elif "even" in BetType or "odd" in BetType or "low" in BetType or "high" in BetType:
            Multiplier=2 

        elif "practice" in BetType : 
            BetType="None"
            print("A practice game of roulette will play...")

        else :
            print("An Error occured please retry...")
            successful=False

        #if the Setup was successful a Game of Roulette starts
        if successful :
            print("Bet is set to",BetType)
            print("Playing a Game of Roulette")
            Reward=BetAmount*Multiplier
            break

    #If the Setup Attempt was uncessful 3 times in a row, an error message pops up     
    else :
        print("The Game couldn't load 3 times in a row, please restart the program...")



    if successful :
        #Choosing a random number
        RouletteNumbers={0 : "green" ,1 : "red",2 : "black", 3 : "red", 4 : "black", 5 : "red", 6 : "black", 7 : "red", 8 : "black", 9 : "red", 10 : "black", 11 : "black", 12 : "red", 13 : "black", 14 : "red", 15 : "black", 16 : "red", 17 : "black", 18 : "red", 19 : "red", 20 : "black", 21 : "red", 22 : "black", 23 : "red", 24 : "black", 25 : "red", 26 : "black", 27 : "red", 28 : "black", 29 : "black", 30 : "red", 31 : "black", 32 : "red", 33 : "black", 34 : "red", 35 : "black", 36 : "red"}
        Roulette=choice(list(RouletteNumbers.items()))

        #Announcing the result to the player, then calculates the Reward with a function
        print("The ball landed on a  : ",Roulette)

        #PROCESSING ALL THE DATA

        #Data Setup : Separates the two values of the Roulette tuple and sets Win status to true by default
        RouletteNumberOutput=int(Roulette[0])
        RouletteColorOutput=Roulette[1]
        Win=True

        #Determines wheter the player won or not
        if BetNumber in Roulette or BetColor in Roulette or ("odd" in BetType and RouletteNumberOutput%2==1) or ("even" in BetType and RouletteNumberOutput%2==0) or ("low" in BetType and 0<RouletteNumberOutput<=18) or ("high" in BetType and 18<RouletteNumberOutput<=36):
                print("Congratulations ! (You just made :",Reward,"Casino chips)")

        elif BetType=="None" :
                print("Well you don't get anything... It's a practice game...")
                BetAmount=0
        else :
                Win=False
                print("What a bust ! (You just lost :",BetAmount,"Casino chips)")
            
        from Data.InventoryManagement.MoneyManagement.money import gain

        #Updates the Player's Balance to reflect the what they won/lost
        gain(Reward,BetAmount,Win,Player)

    else : 
        Roulette : tuple = ('error','error')

    return {
            'Result' : Roulette,
            'Win' : Win,
            'Reward' : Reward,
        }

    
        