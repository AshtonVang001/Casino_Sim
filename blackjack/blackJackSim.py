from blackjack.blackJackRules import Rules

class Simulation(Rules):
    def __init__ (self, test):
        self.test = test


    r = Rules()
    r.money = int(input("Enter your buy in: "))

    #user places bet
    #dealer deals 2 cards to player (face up) and 2 cards to himself (1 face up and 1 face down)
    #player can choose to hit or stand
    #if player hits and busts round is over
    #if player stands or hits then stands then it is the dealers turn
    #dealer reveals second card
    #dealer must hit if they are < 17
    #dealer must stand if they are >= 17
    #if dealer busts player wins
    #if player busts they lose
    #if neither bust whoever has the highest number wins
    #if player wins they 2x their money
    #if player hits 21 w first 2 cards it is a 3:2 payout
