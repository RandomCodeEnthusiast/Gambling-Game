#The money management system of the Gambling Game
#NOTE : NEEDS COMMENTS

from InventoryManagement.BackUpSystem.BackUp import FileBackUp
from config import projectpath

savepath : str = projectpath() + r'\InventoryManagement\MoneyManagement'
moneysavepath : str = savepath + r'\moneysave.txt'
moneysavename : str ='moneysave.txt'

def gain(Reward,BetAmount : int | float,GameWin : bool,Player : int) -> None :

    '''Updates a Player's Balance after a game.         
    Note : Doesn't show the new balance'''

    OldMoneyCounter=Money(Player)
    Benefit=Reward-BetAmount 
    if GameWin:
        MoneyCounter=OldMoneyCounter+Benefit
    else :
        MoneyCounter=OldMoneyCounter-BetAmount
    
    MoneyModifier(Player, OldMoneyCounter, MoneyCounter)
    

def Money(Player : int) -> int | float :

    '''Returns how much money the desired player has'''

    FileBackUp(moneysavepath,moneysavename)
    with open(moneysavepath, 'r' ) as save:
        MoneySave=save.readlines()
        MoneyCounter=float(MoneySave[Player-1])

        return MoneyCounter
    
def MoneyModifier(Player : int, OldMoneyCounter : int | float, MoneyCounter : int | float) -> None :
    
    '''A function that modifies the MoneyCounter of the desired player'''

    FileBackUp(moneysavepath,moneysavename)

    with open(moneysavepath, 'r') as r :
        NewSave = r.readlines()

    with open(moneysavepath, 'w' ) as save:
        for line in range (len(NewSave)) :
            if line==Player-1 :
                SaveOverwrite=NewSave[line].replace(str(OldMoneyCounter), str(MoneyCounter))
            else :
                SaveOverwrite=NewSave[line]
            save.write(SaveOverwrite)