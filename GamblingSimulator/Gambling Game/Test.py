from time import sleep
from datetime import datetime,timedelta

from WishingSim.WishSystem import Wish
from InventoryManagement.StoneManagement.Stone import StoneBuy,StoneCheck
from InventoryManagement.MoneyManagement.money import Money
from InventoryManagement.MoneyManagement.Daily import Daily
from project import projectpath ; from os import remove

Player : int = 2 #REMOVE when moving to main



Action : str = str(input('What do you want to do : ')).lower()

if 'wish' in Action or 'pull' in Action :

    WishCount : int = int(input("How many times do you want to wish : "))
    Wish(Player,WishCount) ; print() ; sleep(0.2)

elif 'buy' in Action :

    BuyAmount = int(input('How many stones do you want to buy : '))
    StoneBuy(BuyAmount, Player)

elif 'check' in Action :
    StoneCheck(Player)

elif 'daily' in Action :
    Daily(Player)

elif 'folder' in Action :
    for i in range (1,11) :
        GenericPath = projectpath() + r'\WishingSim\Players\Player'
        playerstr = str(i)
        characterfile = r'\5StarCharacters.txt'
        characterfile2 = r'\4StarCharacters.txt'
        p1 = GenericPath + playerstr + characterfile ; p2 = GenericPath + playerstr + characterfile2
        with open(p1, 'w') :
                ...
        with open(p2, 'w') :
                ...
        

elif 'destroy' in Action :
    for i in range(1,11) :
        GenericPath = projectpath() + r'\WishingSim\Players\Player'
        playerstr = str(i) ; print(playerstr)
        characterfile = r'\Characters.txt'
        remove(GenericPath + playerstr + characterfile)
     

print(Money(Player))