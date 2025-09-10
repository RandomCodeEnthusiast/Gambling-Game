#The main file 

from time import sleep

from Data.InventoryManagement.MoneyManagement.money import Money
from Data.InventoryManagement.StoneManagement.Stone import StoneBuy,StoneCheck
from Games.Gacha.GachaSystem import Gacha
from Data.InventoryManagement.MoneyManagement.Daily import Daily


while True :

    NoCount : int = 0
    Player : int = int(input("Which Player is playing : "))
    Funds : float = Money(Player)
    print("You have",Funds,"chips at your disposal") ; sleep (1)
    
    while Funds>0 :

        Funds = Money(Player)
        print(f"You now have {Funds} chips at your disposal") ; sleep (0.5)

        Action : str = str(input("Choose how you want to gamble : ")).lower()
        sleep(1)

        if "blackjack" in Action or "black jack" in Action :
            from Games.BlackJack.BlackJackGame import BlackJackGame
            
            print('Dealer Stands on 17') ; sleep(1)
            BlackJackGame()
            

        elif "roulette" in Action :
            from Games.Roulette.RouletteGame import Roulette_Game
            Roulette_Game(Player)

        elif 'daily' in Action :
            Daily(Player)

        elif 'wish' in Action or 'pull' in Action :

            WishCount : int = int(input("How many times do you want to wish : "))
            Gacha(Player,WishCount) ; print() ; sleep(0.2)

        elif 'buy' in Action :

            BuyAmount = int(input('How many stones do you want to buy : '))
            StoneBuy(BuyAmount, Player)

        elif 'check' in Action :
            StoneCheck(Player)

        elif "don't" in Action or 'no' in Action :
            
            sleep(3) ; print('Do you think you have a choice ?')
            NoCount+=1 ; sleep(3)

            if NoCount>1 :
                print('Fine... You get to leave...') ; sleep(5)
                print('FOR NOW...') ; sleep(5)
                print('The Gambling addiction always catches up...') ; sleep (2)
                break

        else :
            print("This game is not available yet...")

    if Funds==0 :
        print("Too Bad... You lost all of your money gambling")
    