from time import sleep
from datetime import datetime,timedelta

from Data.InventoryManagement.StoneManagement.Stone import StoneBuy,StoneCheck
from Data.InventoryManagement.MoneyManagement.money import Money
from Data.InventoryManagement.MoneyManagement.Daily import Daily
from config import projectpath ; from os import remove

Player : int = 2 #REMOVE when moving to main



Action : str = str(input('What do you want to do : ')).lower()



if 'folder' in Action :
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