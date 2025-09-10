#Imports
from config import projectpath

#Setting up the paths to open files
stonecountpath = projectpath() + r'\Data\InventoryManagement\StoneManagement\Stonesave.txt'
stonesavename = 'Stonesave.txt'

def StoneBuy(BuyAmount :int, Player : int) -> None :
    
    '''Buys a desired amount of stones for a certain player if they have sufficient funds '''
    
    from Data.InventoryManagement.MoneyManagement.money import MoneyModifier,Money

    #Defining the Funds of the Player
    Funds = Money(Player)

    #Calculating how much the player would be spending
    BuyCost = 100
    Spending = BuyAmount*BuyCost

    #Checks if the Player has enoguh to buy the amount of stones they want
    if Funds >= Spending :
        NewFunds = Funds - Spending
        StoneModifier(BuyAmount,Player,Spend=False)
        MoneyModifier(Player,Funds,NewFunds)
        print(f'You now have {NewFunds} in Gambling Funds')

    else :
        print('Insufficient Funds...')

def StoneModifier(ModifyAmount :int,Player : int,Spend :bool) -> None :

    '''Spends or Adds the desired amount of stones for the desired player'''

    #Checks how many Stones the Player HAD
    with open (stonecountpath, 'r') as f :
        Stonesave =  f.readlines()
        OldStoneCount = int(Stonesave[Player-1]) 

    #Tries to modify the StoneCount by the designated amount
    #If the player doesn't have enough(spend mode) prints an error message
    try :
        if Spend :
            if OldStoneCount >= ModifyAmount :
                StoneCount = OldStoneCount - ModifyAmount
            else :    
                raise Exception  
        else :
            StoneCount = OldStoneCount + ModifyAmount
    except :
        if Spend :
            print(f'You are missing {ModifyAmount-OldStoneCount} Stones to proceed')
            return None
        else : 
            print('An Error Occured') #Figure out later how to manage

    #Rewrites the save and updates the StoneCount of the designated Player
    with open (stonecountpath, 'w') as f :
        for line in range (len(Stonesave)) :
            if line==Player-1 :
                SaveOverwrite=Stonesave[line].replace(str(OldStoneCount), str(StoneCount))
            else :
                SaveOverwrite=Stonesave[line]
            f.write(SaveOverwrite)

def StoneCheck(Player : int) -> int : 

    '''Checks the StoneCount of the desired player'''

    #Opening the file where the Stone count for each player is stored and reading the desired one
    with open (stonecountpath, 'r') as f :
        Stonesave = f.readlines()
        StoneCount = int(Stonesave[Player-1])
    return StoneCount