def BlackJackGame() :

    from os import remove

    from GeneralSetup import BetAmountSetup
    from InventoryManagement.MoneyManagement.money import gain
    from project import projectpath

    Dealer=True
    Player=False
    print('Please separate the player numbers by a space, else an error will occur')
    PlayerCount=[int(x) for x in input("Which players for this game of BlackJack : ").split()]
    PlayerBetAmount = []

    for idx, PlayerNumber in enumerate(PlayerCount):
        BetAmount = BetAmountSetup(PlayerNumber)
        PlayerBetAmount.append(BetAmount)
    

    DealerScore : int=BlackJackSetup(Dealer)
    DealerActive = True

    PlayerScores = []
    PlayerActive = [True] * len(PlayerCount)
    PlayerRewards = [0] * len(PlayerCount)
    PlayerBlackJack = []
    Turn = 0

    # Initial card draw for each player
    for idx, PlayerNumber in enumerate(PlayerCount):
        print("Drawing the Cards for Player :", PlayerNumber)
        PlayerScore=BlackJackSetup(Player)
        PlayerScores.append(PlayerScore)
        

    # Main game loop: one action per round for dealer and each player
    while DealerActive or any(PlayerActive):

        Turn+=1

        # Dealer's turn (one action)
        if DealerScore > 21 :
            DealerActive=False
            print("Dealer stands.")
        if DealerActive:
            print("\nDealer's turn.")
            if 22>DealerScore>=17 :
                print("Dealer stands.")
                DealerActive=False
            elif DealerScore>21 :
                DealerActive=False
            else :
                Show=False
                DealerScore=Draw(1,Show,DealerScore)
                print("Dealer draws.")
                if DealerScore>=17 and DealerScore<=21 :
                    print("Dealer stands.")
                    DealerActive=False

        # Each player's turn (one action)
        for idx, PlayerNumber in enumerate(PlayerCount):
            if not PlayerActive[idx]:
                continue
            PlayerScore = PlayerScores[idx]
            print(f"\nPlayer {PlayerNumber}'s turn. Current score: {PlayerScore}")

            if Turn==1 :
                if PlayerScore==21 :
                    print("You got a BlackJack !")
                    BlackJack=True
                    PlayerActive[idx]=False
                    continue
                else :
                    BlackJack=False
                PlayerBlackJack.append(BlackJack)

            if PlayerScore>21 :
                print(f"Player {PlayerNumber} busted!")
                PlayerActive[idx]=False
                continue

            try :
                if Turn==1 :
                    decision=str(input(f"Player {PlayerNumber}, what do you want to do (Fold/Hit/Double Down): ")).lower()
                else :
                    decision=str(input(f"Player {PlayerNumber}, what do you want to do (Fold/Hit): ")).lower()
                if "fold" in decision :
                    PlayerActive[idx]=False
                elif "hit" in decision :
                    PlayerScore=hit(PlayerScore)
                    print("New score:", PlayerScore)
                    PlayerScores[idx]=PlayerScore
                    if PlayerScore>=21 :
                        PlayerActive[idx]=False
                elif ("double down" in decision or "doubledown" in decision) and Turn==1 :
                    PlayerScore=Draw(1,True,PlayerScore)
                    BetAmount*=2
                    print("New score after Double Down:", PlayerScore)
                    PlayerScores[idx]=PlayerScore
                    PlayerActive[idx]=False
                else :
                    print("Invalid action. You lose your turn.")
            except Exception as e:
                print("An Error occurred... Please retry", e)

    # Determine rewards after all are done
    if DealerScore>21 :
        print("The Dealer Busted !")
    print(f"The dealer got a Score of {DealerScore}")
    for idx, PlayerNumber in enumerate(PlayerCount):
        PlayerScore = PlayerScores[idx]
        BetAmount = PlayerBetAmount[idx]
        if PlayerBlackJack[idx] :
            Multiplier=2.5
        else :
            Multiplier = 2 
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

        PlayerRewards[idx]=Reward
        print(f"Player {PlayerNumber} reward: {Reward}")
        gain(Reward,BetAmount,GameWin,PlayerNumber)


    remove(projectpath() + r"\CardDeck\RemainingCards.txt")
     
    


#Draws one or multiple cards,
#uses the function CardValue to determine value, 
#adds it to the Score with function ScoreCalc

def Draw(DrawAmount,Show,Score : int) :

    from CardDeck.GCardSelector import RandomCard

    for x in range(DrawAmount) :
            Drawn=RandomCard()
            DrawnValue=CardValue(Drawn,Show)
            Score=ScoreCalc(DrawnValue,Drawn,Score)

    return Score


#Calculates the value of a Card, deciding whether or not to show the card drawn and it's value

def CardValue(Drawn,Show) :
    
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



#Calculates the Score based of the Card drawn and it's value, as well as the previous score

def ScoreCalc(DrawnValue,CardDrawn,Score : int):
    Score = 0 if Score is None else int(Score)
    Score=Score+DrawnValue

    #Temporary : 
    Aces=0

    if "Ace" in CardDrawn :
            Aces+=1
    while Aces>0 and Score>21 :
            Score-=10
            Aces-=1
    return Score
    
def BlackJackSetup(Dealer) :
    Show=True
    Score : int = 0
    if Dealer :
        DrawAmount=1
        print("Drawing the dealer's Cards...")
        Score=Draw(DrawAmount,Show,Score)
        Show=False
        Score=Draw(DrawAmount,Show,Score)
    else :
        DrawAmount=2
        Score=Draw(DrawAmount,Show,Score)
    
    return Score



def hit(Score) :

    DrawAmount=1
    Show=True
    Score=Draw(DrawAmount,Show,Score)

    return Score



