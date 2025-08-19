#The main file 

from time import sleep

from InventoryManagement.MoneyManagement.money import Money


while True :
    NoCount=0
    Player=int(input("Which Player is playing : "))
    Funds=Money(Player)
    while Funds>0 :
        print("You have",Funds,"chips at your disposal") ; sleep (1)
        GamePlayed=str(input("Choose how you want to gamble : ")).lower()
        sleep(2)
        if "blackjack" in GamePlayed or "black jack" in GamePlayed :
            from BlackJack.BlackJackGame import BlackJackGame
            BlackJackGame()
            pass
        elif "roulette" in GamePlayed :
            from Roulette.RouletteSetup import Roulette_Setup
            Roulette_Setup(Player)
            pass
        elif "don't" in GamePlayed or 'no' in GamePlayed :
            sleep(3) ; print('Do you think you have a choice ?')
            NoCount+=1 ; sleep(5)
            pass
            if NoCount>1 :
                print('Fine... You get to leave...') ; sleep(5)
                print('FOR NOW...') ; sleep(5)
                print('The Gambling addiction always catches up...') ; sleep (5)
                print('All roads lead to Rome...........') ; sleep (1)
                break

        else :
            print("This game is not available yet...")

    if Funds==0 :
        print("Too Bad... You lost all of your money gambling")
