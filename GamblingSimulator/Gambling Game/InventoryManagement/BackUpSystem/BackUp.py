#NOTE : NEEDS MORE/BETTER COMMENTS

def FileBackUp(FilePath : str, FileName : str ) :

    '''
    Backs up the desired file.
    Please go to the file for example of inputs
    Note : This function is only made for .txt files, it will fail otherwise
    '''
    #FileName example : File.txt
    #FilePath example : C:\Users\Username\Folder\PROJECTFOLDERNAME\Gambling Game\InventoryManagement\BackUpSystem\moneysaveBackup.txt

    from project import projectpath
    
    BackUpFolder = projectpath() + r'\InventoryManagement\BackUpSystem\ '[:-1]
    
    with open (FilePath,'r') as r :
        FileBackUpPath :str = BackUpFolder + FileName[:-4] + "Backup.txt"
        text = r.readlines()
        with open(FileBackUpPath,'w') as w :
            for x in range (len(text)) :
                w.write(text[x])

def FileOpener(FilePath : str) -> list :

    '''Returns the contents of the file as a list.'''

    with open(FilePath, 'r') as f :
        text : list = f.readlines()


    return text

def FileElementReplacer(FilePath : str,ToReplace,Replacing,ChangingLine) : 
    #WORK IN PROGRESS, PLEASE IMPLEMENT IN THE REST OF THE PROJECT SOON

    '''Replaces one element of a file on a specific line'''

    text = FileOpener(FilePath)
    LineCount = len(text)
    #ADD BACKUP LATER
    with open(FilePath, 'w') as f : 
        for saveline in range(LineCount) : 
            if saveline == ChangingLine :
                SaveOverwrite = text[saveline].replace(str(ToReplace), str(Replacing))
                if SaveOverwrite == text[saveline] :
                    print("The text that was supposed to be replaced wasn't : this is an Error, please investigate further ")
            else :
                SaveOverwrite = text[saveline]
            f.write(SaveOverwrite)
            
def FileAppender(FilePath : str,Appending : str) :
    with open(FilePath, 'a') as f :
        f.write(Appending)

def FileWriter(FilePath : str,Writing : str) :

    '''Note : if the file already exist it will be overwritten'''

    with open(FilePath, 'w') as f :
        f.write(Writing)