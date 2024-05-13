import random

# 1 is Ace, 2-10 is number cards, 11, 12, 13 are J Q K.
cards = [str(i) + "_" + str(j) 
         for i in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] 
         for j in ["S", "H", "D", "C"]]

class Player:
    def __init__(self) -> None:
        self.points = 100
        self.hands = []

class AI:
    def __init__(self) -> None:
        self.name = "John"
        self.points = 100
        self.hands = []
    
    def bet():
        bet = 0
        return bet
    
class Dealer:
    def __init__(self) -> None:
        self.cards = cards
    
    def pickCards(self):
        cardAmount = 51
        rnd = random.randint(0, cardAmount)
        card = self.cards.pop(rnd)
        cardAmount -= 1
        return card
    
    def reset(self):
        self.cards = cards

def gameStart() -> None:
    print("Starting Texas Holdem Poker!\n\nPlease Choose the mode of a game!")
    while True:
        mode = input("Choose between aivai and pvai. If you are not aware of the rule, please type 'help': ").lower()
        while mode not in ["aivai", "pvai", "help"]:
            mode = input("Wrong option, please choose between: aivai, pvai, help: ").lower()
            
        dealer = Dealer()
        groundCards = []
        cb = 0
        win = None
        
        if mode == 'aivai':
            players = [AI(), AI(), ...]
            print("Starting AI v AI Mode...")
            for p in players:
                p.hands.append(dealer.pickCards())
                p.hands.append(dealer.pickCards())
                
            # Pre-flop
            for p in players:
                if cb == 0:
                    decision = p.bet()
                    continue
                    
                while cb != p.bet():
                    # AI decided to die / give up.
                    if decision != -1:
                        cb = decision
                    else:
                        players.pop(players.index(p))
            
            if len(players) <= 1:
                win = players[0]
                
            for p in players:
                pass
            
        elif mode == 'pvai':
            p1 = Player()
            p2 = AI()
            
        elif mode == 'help':
            print("This is a poker game!")

if __name__ == "__main__":
    gameStart()