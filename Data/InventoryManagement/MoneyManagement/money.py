#The money management system of the Gambling Game
#NOTE : NEEDS COMMENTS

from Data.InventoryManagement.BackUpSystem.BackUp import FileBackUp
from config import projectpath

savepath : str = projectpath() + r'\Data\InventoryManagement\MoneyManagement'
moneysavepath : str = savepath + r'\moneysave.txt'
moneysavename : str ='moneysave.txt'

def gain(Reward : float,BetAmount : float,GameWin : bool,Player : int) -> None :

    '''Updates a Player's Balance after a game.         
    Note : Doesn't show the new balance'''

    OldMoneyCounter=Money(Player)
    Benefit=Reward-BetAmount 
    if GameWin:
        MoneyCounter=OldMoneyCounter+Benefit
    else :
        MoneyCounter=OldMoneyCounter-BetAmount
    
    MoneyModifier(Player, OldMoneyCounter, MoneyCounter)
    

def Money(Player : int) -> float :

    '''Returns how much money the desired player has'''

    FileBackUp(moneysavepath,moneysavename)
    with open(moneysavepath, 'r' ) as save:
        MoneySave=save.readlines()
        MoneyCounter=float(MoneySave[Player-1])

        return MoneyCounter
    
def MoneyModifier(Player : int, OldMoneyCounter : float, MoneyCounter : float) -> None :
    
    '''A function that modifies the MoneyCounter of the desired player'''

    FileBackUp(moneysavepath,moneysavename)

    with open(moneysavepath, 'r') as r :
        NewSave = r.readlines()

    with open(moneysavepath, 'w' ) as save:
        for line in range (len(NewSave)) :
            if line==Player-1 :
                SaveOverwrite = f"{MoneyCounter}\n"
            else :
                SaveOverwrite=NewSave[line]
            save.write(SaveOverwrite)