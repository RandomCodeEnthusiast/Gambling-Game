
#Imports
from config import projectpath
from InventoryManagement.BackUpSystem.BackUp import FileBackUp,FileOpener
from InventoryManagement.MoneyManagement.money import Money,MoneyModifier

#Seting up paths for opening files
projectfolder = projectpath()
savepath : str = projectfolder + r'\InventoryManagement\MoneyManagement'
dailysavepath : str = savepath + r'\Daily.txt'
dailysavename : str = 'Daily.txt'

def Daily(Player) :

    '''A Daily loggin system, rewards the Player with a fix amount + a Bonus based on their characters'''

    from datetime import datetime,timedelta

    #Backing up the dailytime save file
    with open(dailysavepath, 'r' ) as f :
        dailytimesave = f.readlines()
        FileBackUp(dailysavepath,dailysavename)

    #Checking when the player last claimed their logging bonus 
    try :

        UsefulSaveline = dailytimesave[Player-1][:-1]
        if str(UsefulSaveline) != '0' :
            OldDailytime : datetime = datetime.strptime(UsefulSaveline, r'%Y-%m-%d %H:%M:%S.%f')    
        
        #Used to not cause later Errors if the time is equal to '0'
        else :
            raise RuntimeError

    #Used to set a far away time if it's the Player's first loggin     
    except RuntimeError :

        OldDailytime : datetime = datetime(year=2025,month=8,day=22,hour=21)
    
    #Getting the Current Time, and creating the RequiredTime variable : one day after last loggin
    Time : datetime = datetime.now()
    RequiredTime : datetime = OldDailytime + timedelta(days = 1)
    lines : int = len(dailytimesave)

    #Comparing the Current Time to the Required Time : 
    #if the time meets the requirements the OldDailyTime is replaced by the Current Time 
    #NOTE : CHANGE THE FILE OPENING WITH THE Function designed for it
    if Time >= RequiredTime : 
        with open(dailysavepath, 'w') as f :
            for saveline in range(lines) :

                if saveline == Player-1 :

                    if OldDailytime == datetime(year=2025,month=8,day=22,hour=21) :
                        ToReplace = 0

                    else : 
                        ToReplace = OldDailytime
                        print(ToReplace)

                    NewSave = dailytimesave[saveline].replace(str(ToReplace), str(Time))
                
                else :
                    NewSave = dailytimesave[saveline]

                f.write(NewSave)

        successful = True

    #If the Time doesn't meet the requirements, the user is informed by how much time they logged in too early 
    else :
        print(f'You checked in too early by {RequiredTime-Time}')
        successful = False

    #Adds Money to the Player's Balance if their loggin meets the requirements 
    # (1 day after the last succesful one)
    if successful :

        Bonus = DailyBonus(Player) 
        OldFunds = Money(Player)
        NewFunds = OldFunds + 1000 + Bonus
        MoneyModifier(Player,OldFunds,NewFunds)

def DailyBonus(Player : int) -> int :

    '''Calculates the Bonus to add to Daily loggin reward.      
    Based on the number of unique characters, duplicates and their rarity'''

    #Setting up paths to open files
    PlayerFolder : str = r'\Players\Player' + str(Player)
    path1 = projectfolder + r'\WishingSim' + PlayerFolder
    
    #Setting up the data to calculate the money bonus for 4* characters
    EpicList = FileOpener(path1 + r'\4StarCharacters.txt')
    ELineNumber = len(EpicList) ; UniqueEpics = ELineNumber
    NoEpics = False ; DuplicateEpicCount = 0
    
    #Calculating the money bonus due to 4*
    for Line in range(ELineNumber) : 
        if ELineNumber == 0 :
            NoEpics = True ; break
        
        EQuantity = int(EpicList[Line][0])

        if EQuantity > 1 :
            DuplicateEpicCount += EQuantity - 1
    
    if NoEpics :
        EpicsBonus = 0
    else :
        EpicsBonus = 10*UniqueEpics + 5*DuplicateEpicCount

    #Same thing but for 5*
    LegendaryList = FileOpener(path1 + r'\5StarCharacters.txt')
    LegLineNumber = len(LegendaryList) ; UniqueLegs = LegLineNumber
    NoLegs = False ; DuplicateLegendaryCount = 0

    #Calculating for 5*
    for Line in range(1,LegLineNumber) :
        if LegLineNumber == 0 :
            NoLegs = True ; break

        LQuantity = int(LegendaryList[Line-1][0])
        
        if LQuantity > 1 :
            DuplicateLegendaryCount += LQuantity - 1

    if NoLegs :
        LegendariesBonus = 0
    else : 
        LegendariesBonus = 100*UniqueLegs + 50*DuplicateLegendaryCount

    #Calculating the final Bonus and returning it
    Bonus = EpicsBonus + LegendariesBonus
    return Bonus