#The setup of RouletteSim

def Roulette_Setup(Player) : 

    for i in range (3) : 

        from GeneralSetup import BetAmountSetup
        from GeneralSetup import BetTypeSetup

        BetAmount=BetAmountSetup(Player)
        BetType=BetTypeSetup()
        successful=True

        BetColor="None"
        BetNumber=[69]

        if BetType=="color" : 
            BetColor=input("Bet Color : ").lower()
            Multiplier=2

        elif "number" in BetType: 
            print("Please input numbers beetween 0 and 36, otherwise you will not gain anything")
            BetNumber=[int(x) for x in input("Bet Number(s) : ").split()]
            Multiplier=36/len(BetNumber) 

        #NOTE : This isn't the the Split or Square BetType because numbers aren't adjacent

        elif "even" in BetType or "odd" in BetType or "low" in BetType or "high" in BetType:
            Multiplier=2 

        elif "practice" in BetType : 
            BetType="None"
            print("A practice game of roulette will play...")

        else :
            print("An Error occured please retry...")
            successful=False

        if successful :
            print("Bet is set to",BetType)
            print("Playing a Game of Roulette")
            Reward=BetAmount*Multiplier

            from Roulette.RouletteSim import Roulette_Sim
            Roulette_Sim(BetType,BetNumber,BetColor,BetAmount,Reward,Player)
            
            break
            
    else :
        print("The Game couldn't load 3 times in a row, please restart the program...")