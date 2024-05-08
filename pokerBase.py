import random

class Player:
    def __init__(self) -> None:
        pass

class AI:
    def __init__(self) -> None:
        pass
    
    def bet():
        pass
    
    def call():
        pass

def gameStart() -> None:
    print("Starting Texas Holdem Poker!\n\nPlease Choose the mode of a game!")
    while True:
        gameMode = input("Choose between aivai and pvai. If you are not aware of the rule, please type 'help'.")
        if gameMode.lower() == "aivai":
            pass
        elif gameMode.lower() == "pvai":
            pass
        elif gameMode.lower() == "help":
            pass
        else:
            print("Wrong Input detected. Please try again.")
    pass

if __name__ == "__main__":
    gameStart()