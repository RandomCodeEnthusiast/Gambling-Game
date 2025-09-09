#NOTE : NEEDS MORE COMMENTS

def BlackJackGame() :

    '''Launches a game of BlackJack and at the end saves the rewards for all players'''

    #Imports
    from os import remove

    from GeneralSetup import BetAmountSetup
    from Data.InventoryManagement.MoneyManagement.money import gain,Money
    from config import projectpath
    from Data.InventoryManagement.BackUpSystem.BackUp import FileWriter

    #Setup : asking which player(s) is (are) playing, and creating other variables
    Dealer=True
    Player=False
    print('Please separate the player numbers by a space, else an error will occur')
    PlayerCount=[int(x) for x in input("Which players for this game of BlackJack : ").split()]
    FileWriter(FilePath = projectpath() + r'\BlackJack\PlayerCount.txt',Writing = str(len(PlayerCount)))
    PlayerBetAmount = []

    # Iniating the Aces.txt file
    FileWriter(projectpath() + r'\BlackJack\Aces.txt', '\n'.join(['0'] * len(PlayerCount)))

    #Asking each player how much they want to bet
    for PlayerOrder, PlayerNumber in enumerate(PlayerCount):
        BetAmount = BetAmountSetup(PlayerNumber)
        PlayerBetAmount.append(BetAmount)
    
    #Drawing the Dealer's First two cards (showing only one)
    DEALER_POSITION : int = 0
    DealerScore : int=BlackJackSetup(Dealer,DEALER_POSITION)
    DealerActive = True

    #Setting up a bunch of list variables for managing player data
    PlayerScores = []
    PlayerActive = [True] * len(PlayerCount)
    PlayerRewards = [0] * len(PlayerCount)
    PlayerBlackJack = []
    Turn = 0

    #Initial card draw for each player
    for PlayerOrder, PlayerNumber in enumerate(PlayerCount):
        print("Drawing the Cards for Player :", PlayerNumber)
        PlayerScore=BlackJackSetup(Player,PlayerOrder + 1) #Adding 1 to PlayerOrder for acecount saving
        PlayerScores.append(PlayerScore)
        

    
    
    #Main game loop: one action per round for dealer and each player
    while any(PlayerActive):

        Turn+=1

        #Each player's turn (one action)
        for PlayerOrder, PlayerNumber in enumerate(PlayerCount):
            if not PlayerActive[PlayerOrder]:
                continue
            PlayerScore = PlayerScores[PlayerOrder]
            print(f"\nPlayer {PlayerNumber}'s turn. Current score: {PlayerScore}")

            #Checking if BlackJack on 1st Turn
            if Turn==1 :

                if PlayerScore==21 :
                    print("You got a BlackJack !")
                    BlackJack=True
                    PlayerActive[PlayerOrder]=False
                    PlayerBlackJack.append(BlackJack)
                    continue

                else :
                    BlackJack=False
                    PlayerBlackJack.append(BlackJack)

            if PlayerScore>21 :
                print(f"Player {PlayerNumber} busted!")
                PlayerActive[PlayerOrder]=False
                continue

            #Asking the Player what they want to do (Fold/Hit and DoubleDown if it's the 1st Turn)
            successful = False 
            while not successful :
                try :
                    successful = True #Setting succesful to true by default and changing it only when False
                    if Turn==1 :
                        decision=str(input(f"Player {PlayerNumber}, what do you want to do (Fold/Hit/Double Down): ")).lower()
                    else :
                        decision=str(input(f"Player {PlayerNumber}, what do you want to do (Fold/Hit): ")).lower()
                    
                    #Processing the Player input
                    if "fold" in decision :
                        PlayerActive[PlayerOrder]=False

                    elif "hit" in decision :
                        PlayerScore = hit(PlayerScore,PlayerOrder + 1)
                        print("New score:", PlayerScore)
                        PlayerScores[PlayerOrder]=PlayerScore
                        if PlayerScore>=21 :
                            PlayerActive[PlayerOrder]=False

                    elif ("double down" in decision or "doubledown" in decision) and Turn==1 :
                        PlayerScore=Draw(1,True,PlayerScore,False,PlayerOrder + 1) 
                        BetAmount*=2
                        print("New score after Double Down:", PlayerScore)
                        PlayerScores[PlayerOrder]=PlayerScore
                        PlayerActive[PlayerOrder]=False

                    else :
                        print("Invalid action.")
                        successful = False

                except Exception as exc :
                    print("An Error occurred... Please retry", exc)

    #Dealer's time to play after every player stopped playing
    DealerTurn = 0
    while DealerActive :
        DealerTurn += 1

        if DealerScore > 21 :
            DealerActive=False
            print("Dealer Busted.")
        
        if DealerActive:
            print("\nDealer's turn.")
            
            if 22>DealerScore>=17 :
                print("Dealer stands.")
                DealerActive=False
            elif DealerScore>21 :
                DealerActive=False
            else :
                Show=False
                DealerScore=Draw(1,Show,DealerScore,False,DEALER_POSITION)
                print("Dealer draws.")
                if DealerScore>=17 and DealerScore<=21 :
                    print("Dealer stands.")
                    DealerActive=False

    #Determine rewards for each player at the end of the game
    if DealerScore>21 :
        print("The Dealer Busted !")
    print(f"The dealer got a Score of {DealerScore}")

    #Creating a loop to account for each player
    for PlayerOrder, PlayerNumber in enumerate(PlayerCount):
        PlayerScore = PlayerScores[PlayerOrder]
        BetAmount = PlayerBetAmount[PlayerOrder]
        
        #Determines the multiplier : if BlackJack or Not
        print(PlayerOrder)

        if PlayerBlackJack[PlayerOrder] :
            Multiplier=2.5
        else :
            Multiplier = 2 

        #Determines wheter or not and Player won and modifies the variable Gamewin accordingly
        GameWin=True
        if PlayerScore>21 :
            print(f"Player {PlayerNumber} busted!")
            GameWin=False

        elif DealerScore>21 or PlayerScore>DealerScore :
            print(f"Player {PlayerNumber} wins!")
            Reward=BetAmount*Multiplier

        elif PlayerScore==DealerScore :
            print(f"Player {PlayerNumber} ties with the dealer.")
            Reward=BetAmount
        else :
            print(f"Player {PlayerNumber} loses.")
            GameWin=False

        if not GameWin :
            Reward = 0

        #Updating each Player's Balance after the Game
        PlayerRewards[PlayerOrder]=Reward
        print(f"Player {PlayerNumber} reward: {Reward}")
        gain(Reward,BetAmount,GameWin,PlayerNumber)
        print(f'You now have {Money(Player)} in funds')

    #Removes the RemainingCards file to reset the deck and other files created just for the game
    remove(projectpath() + r"\CardDeck\RemainingCards.txt")
    remove(projectpath() + r'\BlackJack\Aces.txt')
    remove(projectpath() + r'\BlackJack\PlayerCount.txt')
         


def Draw(DrawAmount,Show,Score : int,Start : bool,PlayerPosition) :

    '''
    Draws one or multiple cards,
    uses the function CardValue to determine value, 
    adds it to the Score with function ScoreCalc
    '''

    from CardDeck.GCardSelector import RandomCard

    for x in range(DrawAmount) :
            Drawn=RandomCard()
            DrawnValue=CardValue(Drawn,Show)
            Score=ScoreCalc(DrawnValue,Drawn,Score,PlayerPosition)

    return Score



def CardValue(Drawn,Show) -> int :

    '''Calculates the value of a Card, deciding whether or not to show the card drawn and it's value'''

    CardDrawn : str=Drawn[0]+Drawn[1]+Drawn[2]
    
    try :
        DrawnValue=int(CardDrawn)
    except:
        if "Ace" in CardDrawn :
            DrawnValue=11
        else :
            DrawnValue=10

    if Show :
        print ("Card Value is :",DrawnValue)
        print (Drawn)
    return DrawnValue



def ScoreCalc(DrawnValue, CardDrawn, Score: int, PlayerPosition):
    '''Calculates the Score based of the Card drawn and it's value, as well as the previous score'''

    from Data.InventoryManagement.BackUpSystem.BackUp import FileOpener

    Score = 0 if Score is None else int(Score)
    Score += DrawnValue

    # Use PlayerPosition directly, no offset
    try:
        Aces = CheckAces()[PlayerPosition]
    except IndexError:
        Aces = 0
    if "Ace" in CardDrawn:
        Aces += 1
    while Aces > 0 and Score > 21:
        Score -= 10
        Aces -= 1
    SaveAces(PlayerPosition, Aces)

    return Score

def SaveAces(PlayerPosition: int, Aces: int):
    from Data.InventoryManagement.BackUpSystem.BackUp import FileOpener, FileWriter
    from config import projectpath

    # Get player count as integer
    PlayerCount = int(FileOpener(projectpath() + r'\BlackJack\PlayerCount.txt')[0].strip())
    FilePath = projectpath() + r'\BlackJack\Aces.txt'

    # Read current aces, convert to int and strip newlines
    try:
        PlayerAces = [int(x.strip()) for x in FileOpener(FilePath)]
    except Exception:
        PlayerAces = [0] * PlayerCount

    # Ensure the list is the correct length
    while len(PlayerAces) < PlayerCount + 1 :
        PlayerAces.append(0)

    # Update the ace count for the correct player
    PlayerAces[PlayerPosition] = Aces

    # Write back all ace counts, one per line
    FileWriter(FilePath, '\n'.join(str(x) for x in PlayerAces))

def CheckAces():
    from Data.InventoryManagement.BackUpSystem.BackUp import FileOpener
    from config import projectpath

    FilePath = projectpath() + r'\BlackJack\Aces.txt'
    try:
        PlayerAces = [int(x.strip()) for x in FileOpener(FilePath)]
    except Exception:
        PlayerAces = []
    return PlayerAces


    
def BlackJackSetup(Dealer,PlayerPosition) :

    '''Draws two cards and shows them or not based on who draws (Dealer or Player)'''

    Show=True
    Score : int = 0
    if Dealer :
        DrawAmount=1
        print("Drawing the dealer's Cards...")
        Score=Draw(DrawAmount,Show,Score,True,PlayerPosition)
        Show=False
        Score=Draw(DrawAmount,Show,Score,False,PlayerPosition)
    else :
        DrawAmount=2
        Score=Draw(DrawAmount,Show,Score,True,PlayerPosition)
    
    return Score



def hit(Score,PlayerPosition) :

    '''Makes the Player Draw a Card, showed to everyone, then adds it to the Score'''

    DrawAmount=1
    Show=True
    Score=Draw(DrawAmount,Show,Score,False,PlayerPosition)

    return Score



