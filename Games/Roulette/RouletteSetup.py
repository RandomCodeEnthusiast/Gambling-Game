#The setup of RouletteSim

def Roulette_Setup(Player) : 

    '''The Setup for a game of Roulette : manages all player inputs.
    Calls the Roulette_Sim function at the end.'''

    #Local imports
    from GeneralSetup import BetAmountSetup
    from GeneralSetup import BetTypeSetup
    from Roulette.RouletteSim import Roulette_Sim

    #Done in a loop to account for input errors
    for i in range (3) : 

        #Asking the type (color,number,even,high,etc...), and the amount of the bet
        BetAmount=BetAmountSetup(Player)
        BetType=BetTypeSetup()
        successful=True

        #Setting default values for bet color and number
        BetColor="None"
        BetNumber=[69]

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

            Roulette_Sim(BetType,BetNumber,BetColor,BetAmount,Reward,Player)
            break

    #If the Setup Attempt was uncessful 3 times in a row, an error message pops up     
    else :
        print("The Game couldn't load 3 times in a row, please restart the program...")