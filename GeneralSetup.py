def BetAmountSetup(Player : int) : 

    '''Asks one Player how much they want to bet (with an all in functonnality)'''

    from Data.InventoryManagement.MoneyManagement.money import Money
    Total=Money(Player)

    #Asking the Player how much they want to bet
    BetAmount=(input(f"Bet Amount for Player {Player} : ")).lower()

    #Processing the input with a functionnality for all in
    if "all" in BetAmount :
            BetAmount=Total
    else :
        BetAmount=int(BetAmount)
        if BetAmount>=Total :
            print("Insufficient Funds, set bet to go all in")
            BetAmount=Total
    
    return BetAmount

def BetTypeSetup() :
        
    '''Ask the User the BetType and returns that'''

    BetType=str(input("Bet Type : ")).lower()
    return BetType 