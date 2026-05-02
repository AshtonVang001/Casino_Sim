from blackJackRules import Rules
import random

class Simulation(Rules):
    def __init__ (self, test = 0):
        self.test = test

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

    def play(self):
        r = Rules(10)
        deck = r.deck;
        willPlay = str(input("Would you like to play y/n?"))

        if willPlay == "y":
            r.money = int(input("Enter your buy in: "))
            bet = int(input("Enter bet: "));

            #deal cards
            playerFirstCard = random.choice(list(deck.keys()))
            deck.pop(playerFirstCard)
            dealerFirstCard = random.choice(list(deck.keys()))
            deck.pop(dealerFirstCard);
            playerSecondCard = random.choice(list(deck.keys()))
            deck.pop(playerSecondCard);
            dealerSecondCard = random.choice(list(deck.keys()))
            deck.pop(dealerSecondCard);

            
            playersCards = [playerFirstCard, playerSecondCard];
            dealersCards = [dealerFirstCard, "hidden"]; 
            
            print("Your cards: ")
            print(playersCards)
            print("Dealers cards: ")
            print(dealersCards)

            # keepPlaying = str(input("Would you like to hit or stand? Enter 'h' or 's'"))



player = Simulation();
player.play();

