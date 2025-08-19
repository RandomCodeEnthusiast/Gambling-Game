def FileBackUp(FilePath : str, FileName : str ) :

    '''This function is only made for .txt files, it will fail otherwise'''

    from project import projectpath
    
    BackUpFolder = projectpath() + r'\InventoryManagement\BackUpSystem\ '[:-1]
    
    with open (FilePath,'r') as r :
        FileBackUpPath :str = BackUpFolder + FileName[:-4] + "Backup.txt"
        text = r.readlines()
        with open(FileBackUpPath,'w') as w :
            for x in range (len(text)) :
                w.write(text[x])
