#The money management system of the Gambling Game

from InventoryManagement.BackUpSystem.BackUp import FileBackUp
from project import projectpath

moneysavepath=projectpath() + r'\InventoryManagement\MoneyManagement\moneysave.txt'
moneysavename='moneysave.txt'

def gain(Reward,BetAmount,GameWin,Player) :

    OldMoneyCounter=Money(Player)
    Benefit=Reward-BetAmount 
    if GameWin:
        MoneyCounter=OldMoneyCounter+Benefit
    else :
        MoneyCounter=OldMoneyCounter-BetAmount
    with open(moneysavepath, 'r') as r :
        NewSave = r.readlines()
        with open(moneysavepath, 'w' ) as save:
            for line in range (len(NewSave)) :
                if line==Player-1 :
                    SaveOverwrite=NewSave[line].replace(str(OldMoneyCounter), str(MoneyCounter))
                else :
                    SaveOverwrite=NewSave[line]
                save.write(SaveOverwrite)
    print("You now have",MoneyCounter,"chips in gambling funds !")

def Money(Player):
    FileBackUp(moneysavepath,moneysavename)
    with open(moneysavepath, 'r' ) as save:
        MoneySave=save.readlines()
        MoneyCounter=int(MoneySave[Player-1])
        return MoneyCounter
    
