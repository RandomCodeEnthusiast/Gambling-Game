#The Reward Calculation part of the Roulette

def Roulette_Benefit(BetNumber,Roulette,Reward,BetColor,BetAmount,BetType,Player) :
    
    '''Determines the Rewards of a Game of Roulette based on inputs from Roulette_Sim.
    Note : Calls the gain function at the end to save the gains'''

    #Setup : Separates the two values of the Roulette tuple and sets Win status to true by default
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
        
    from InventoryManagement.MoneyManagement.money import gain

    #Updates the Player's Balance to reflect the what they won/lost
    gain(Reward,BetAmount,Win,Player) 