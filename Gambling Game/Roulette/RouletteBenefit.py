#The Reward Calculation part of the Roulette

def Roulette_Benefit(BetNumber,Roulette,Reward,BetColor,BetAmount,BetType,Player) :

    RouletteNumberOutput=int(Roulette[0])
    RouletteColorOutput=Roulette[1]
    Win=True

    if BetNumber in Roulette or BetColor in Roulette or ("odd" in BetType and RouletteNumberOutput%2==1) or ("even" in BetType and RouletteNumberOutput%2==0) or ("low" in BetType and 0<RouletteNumberOutput<=18) or ("high" in BetType and 18<RouletteNumberOutput<=36):
            print("Congratulations ! (You just made :",Reward,"Casino chips)")

    elif BetType=="None" :
            print("Well you don't get anything... It's a practice game...")
            BetAmount=0
    else :
            Win=False
            if BetColor=="black" : 
                print("As expected black always steals your money... (You just lost :",BetAmount,"Casino chips)")
            else : 
                print("What a bust ! (You just lost :",BetAmount,"Casino chips)")
        
    from InventoryManagement.MoneyManagement.money import gain

    gain(Reward,BetAmount,Win,Player) 