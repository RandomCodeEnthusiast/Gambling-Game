def BetAmountSetup(Player : int) : 

    from InventoryManagement.MoneyManagement.money import Money
    Total=Money(Player)

    BetAmount=(input(f"Bet Amount for Player {Player}: ")).lower()

    if "all" in BetAmount :
            BetAmount=Total
    else :
        BetAmount=int(BetAmount)
        if BetAmount>=Total :
            print("Insufficient Funds, set bet to go all in")
            BetAmount=Total
    
    return BetAmount

def BetTypeSetup() :
        BetType=str(input("Bet Type : ")).lower()
        return BetType 