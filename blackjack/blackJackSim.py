from blackJackRules import Rules
import time
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
            money = r.money;
            bet = int(input("Enter bet: "));

            #deal cards
            playerFirstCard = random.choice(list(deck.keys()))
            playerFirstCardVal = deck[playerFirstCard];
            deck.pop(playerFirstCard)

            dealerFirstCard = random.choice(list(deck.keys()))
            dealerFirstCardVal = deck[dealerFirstCard];
            deck.pop(dealerFirstCard);

            playerSecondCard = random.choice(list(deck.keys()))
            playerSecondCardVal = deck[playerSecondCard];
            deck.pop(playerSecondCard);

            dealerSecondCard = random.choice(list(deck.keys()))
            dealerSecondCardVal = deck[dealerSecondCard]
            deck.pop(dealerSecondCard);

            
            playersCards = [playerFirstCard, playerSecondCard];
            dealersCards = [dealerFirstCard, "hidden"]; 

            print("Your cards: ")
            print(playersCards)
            print("Players value: ")
            playerTotal = playerFirstCardVal + playerSecondCardVal;
            print(playerTotal, "\n")
            time.sleep(5)

            print("Dealers cards: ")
            print(dealersCards, "\n")
            time.sleep(5)

            if playerTotal == 21:
                print("You hit blackjack! \n")
                time.sleep(5)
                dealersCards = [dealerFirstCard, dealerSecondCard];
                print("Dealers cards: ")
                print(dealersCards)
                print("Dealers value: ")
                dealerTotal = dealerFirstCardVal + dealerSecondCardVal
                print(dealerTotal, "\n");
                time.sleep(5);
                if dealerTotal == 21:
                    print("It's a tie! You get your money back!")
                    print("You now have a total of $", money);
                else:
                    print("You win!")
                    winnings = bet * 1.5
                    print("You won $", winnings);
                    money += winnings;
                    print("You now have a total of $", money);

            #case here
            

            # keepPlaying = str(input("Would you like to hit or stand? Enter 'h' or 's'"))

            # match keepPlaying:
            #     case playerTotal if playerTotal == 21:
            #         print("You hit 21!")
            #     case playerTotal
            
            # print("Dealers value: ")
            # dealerTotal = dealerFirstCardVal + dealerSecondCardVal
            # print(dealerTotal);
            



player = Simulation();
player.play();

