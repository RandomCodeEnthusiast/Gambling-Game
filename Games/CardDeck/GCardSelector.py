#NOTE : NEEDS MORE COMMENTS

def RandomCard() :

    '''
    Picks a random card out of a standard 52 cards deck. 
    After that it tracks the remaining cards in that deck in RemainingCards.txt  
    Note : Please delete the RemainingCards.txt file after finishing a game
    '''

    from random import randint
    from config import projectpath

    try:
        Cards = projectpath() + r"\CardDeck\RemainingCards.txt"
        with open(Cards, "r") as f:
            lines = f.readlines()
            if not lines:
                raise Exception
    except:
        Cards = projectpath() + r"\CardDeck\Cards.txt"
        with open(Cards, "r") as f:
            lines = f.readlines()

    LineNumber = len(lines)
    Random = randint(0, LineNumber - 1)
    PickedCard = lines[Random]

    # Remove the picked card
    remaining = [line for idx, line in enumerate(lines) if idx != Random]

    with open(projectpath() + r"\CardDeck\RemainingCards.txt", "w") as f:
        f.writelines(remaining)
    return PickedCard