def Gacha(Player : int,WishCount : int) -> None :

    '''Returns a random Loot based on a Rarity and a Pity System '''

    from random import randint
    from time import sleep

    from project import projectpath
    from InventoryManagement.BackUpSystem.BackUp import FileBackUp,FileElementReplacer
    from InventoryManagement.StoneManagement.Stone import StoneModifier,StoneCheck

    #Spends the inputed amount of stones
    if StoneCheck(Player) >= WishCount :
        StoneModifier(WishCount,Player,Spend=True)
    else :
        return None

    #Setup of different variables for files
    PlayerFolder : str = r'\Players\Player' + str(Player)
    txtpath : str = projectpath() + r'\WishingSim'
    PityPath : str = txtpath + PlayerFolder + r'\Pity.txt'
    PityFileName : str = 'Pity.txt'

    for wishes in range (WishCount) : 

        #Looking up what the different pities are :
        with open(PityPath, "r") as f: 
            NewSave = f.readlines()
            OldLegendaryPity : int = int(NewSave[0])
            OldEpicPity : int = int(NewSave[1])

        EpicPityLine : int = 2
        LegendaryPityLine : int = 1

        #Determining the Rarity and updating each pity accordingly
        Rarity = randint(1,1000)

        #Runs if the Rarity is 5*
        if Rarity <= 6 or OldLegendaryPity == 89 :
            print('You just got a 5*') ; sleep(5)
            with open ( txtpath + r'\5star.txt' , 'r' ) as f :

                lines = f.readlines()
                LegendaryPity = 0
                EpicPity = OldEpicPity + 1
                Rarity = '5*'

        #Runs if the Rarity is 4*
        elif 7<=Rarity<=60 or OldEpicPity >= 9 :
            print('You just got a 4*') ; sleep(1)
            with open ( txtpath + r'\4star.txt' , 'r' ) as f :

                lines = f.readlines()
                EpicPity = 0
                LegendaryPity = OldLegendaryPity + 1
                Rarity = '4*'

        #Runs if the Rarity is 3*
        else :
            with open ( txtpath + r'\JunkWeapons.txt' , 'r' ) as f :

                lines : list = f.readlines()
                EpicPity = OldEpicPity + 1
                LegendaryPity = OldLegendaryPity + 1
                Rarity = '3*'

        #Picking which exact reward you will get from the determined rarity
        LineNumber : int = len(lines)
        Pick : int = randint(0, LineNumber - 1)
        PickedLoot : str = lines[Pick]          

        #Pity system (saving to file)
        with open(PityPath, "w") as f:
            
            #Backing up the pity incase of an error
            FileBackUp(PityPath,PityFileName)

            for line in range (len(NewSave)) :
                    
                    if line == EpicPityLine-1 :
                        SaveOverwrite=NewSave[line].replace(str(OldEpicPity), str(EpicPity))

                    elif line == LegendaryPityLine-1 :
                        SaveOverwrite=NewSave[line].replace(str(OldLegendaryPity), str(LegendaryPity))

                    else :
                        SaveOverwrite=NewSave[line]

                    f.write(SaveOverwrite)

        #Saving to logs and printing the picked loot
        GachaLogs(PickedLoot,PlayerFolder,Rarity)
        print(PickedLoot)

        #Pauses if you got a 5* or a 4*, else pauses only a litle. Done for better readability 
        if LegendaryPity == 0 or EpicPity == 0 :
            sleep(2)
        else : 
            sleep(0.2)


def GachaLogs(PickedLoot,PlayerFolder,Rarity) : 

    '''Logs the input(PickedLoot) to The GachaLogs.txt file
    Used to take note of which items the Player got while wishing
    '''

    #Setup : imports and path for opening files
    from InventoryManagement.BackUpSystem.BackUp import FileBackUp,FileElementReplacer,FileAppender,FileOpener
    from project import projectpath
    txtpath = projectpath() + r'\WishingSim' + PlayerFolder

    #Adds the PickedLoot to GachaLogs.txt, along with it's Rarity
    FileAppender(FilePath = txtpath + r"\GachaLogs.txt",Appending = f'{Rarity} : {str(PickedLoot)}')
    
    #Checks if it's a 4*, if it is adds it to the player's save, as new or dupe
    if '4' in Rarity :
        path1 = txtpath + r"\4StarCharacters.txt"
        text = FileOpener(FilePath = path1)
        try :
            Order = text.index(PickedLoot)
            Quantity = int(text[Order][1])
            NewQuantity = Quantity + 1 
            FileElementReplacer(path1, Quantity, NewQuantity, Order)
        except ValueError :
            Appending :str = '1 ' + PickedLoot 
            print(Appending)
            FileAppender(path1,Appending)

    #Same but for 5*    
    elif '5' in Rarity :
        path1 = txtpath + r"\5StarCharacters.txt"
        text = FileOpener(FilePath = path1)
        try :
            Order = text.index(PickedLoot)
            Quantity = int(text[Order][1])
            NewQuantity = Quantity + 1 
            FileElementReplacer(path1, Quantity, NewQuantity, Order)
        except ValueError :
            Appending :str = PickedLoot + '1'
            FileAppender(path1,Appending)
        

    