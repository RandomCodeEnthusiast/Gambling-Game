from project import projectpath

for i in range (1,11) :
        GenericPath = projectpath() + r'\WishingSim\Players\Player'
        playerstr = str(i)
        characterfile = r'\5StarCharacters.txt'
        characterfile2 = r'\4StarCharacters.txt'
        path1 = GenericPath + playerstr + characterfile ; path2 = GenericPath + playerstr + characterfile2
        with open(path1, 'w') :
                ...
        with open(path2, 'w') :
                ...