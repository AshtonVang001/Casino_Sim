from blackJackRules import Rules
import time


class Simulation(Rules):
    def __init__(self):
        super().__init__(money=0)

    def play(self):
        willPlay = input("Would you like to play y/n? ")

        if willPlay != "y":
            return

        self.money = int(input("Enter your buy in: "))
        bet = int(input("Enter bet: "))

        player_hand = []
        dealer_hand = []

        player_hand.append(self.draw_card())
        dealer_hand.append(self.draw_card())
        player_hand.append(self.draw_card())
        dealer_hand.append(self.draw_card())

        player_total = self.calculate_total(player_hand)
        dealer_total = self.calculate_total(dealer_hand)

        print("\nYour cards:")
        print([card for card, value in player_hand])
        print("Player value:", player_total, "\n")
        time.sleep(5)

        print("Dealer cards:")
        print([dealer_hand[0][0], "hidden"], "\n")
        time.sleep(5)

        if player_total == 21:
            print("You hit blackjack! \n")
            time.sleep(5)

            print("Dealer cards:")
            print([card for card, value in dealer_hand])
            print("Dealer value:", dealer_total, "\n")
            time.sleep(5)

            if dealer_total == 21:
                print("It's a tie! You get your money back!")
                print("You now have a total of $", self.money)
            else:
                print("You win!")
                winnings = bet * 1.5
                print("You won $", winnings)
                self.money += winnings
                print("You now have a total of $", self.money)

            return

        while player_total < 21:
            choice = input("Would you like to hit or stand? Enter 'h' or 's': ")

            if choice == "h":
                player_hand.append(self.draw_card())
                player_total = self.calculate_total(player_hand)

                print("\nYour cards:")
                print([card for card, value in player_hand])
                print("Player value:", player_total, "\n")
                time.sleep(5)

                if player_total > 21:
                    print("You lost! \n")
                    time.sleep(5)
                    self.money -= bet
                    print("You have $", self.money)
                    return

            elif choice == "s":
                break

            else:
                print("Invalid choice. Enter 'h' or 's'.")

        print("\nDealer cards:")
        print([card for card, value in dealer_hand])
        print("Dealer value:", dealer_total)
        time.sleep(5)

        while dealer_total < 17:
            dealer_hand.append(self.draw_card())
            dealer_total = self.calculate_total(dealer_hand)

            print("\nDealer hits.")
            print("Dealer cards:")
            print([card for card, value in dealer_hand])
            print("Dealer total:")
            print(dealer_total, "\n")
            time.sleep(5)

        if dealer_total > 21:
            print("You win!")
            time.sleep(5)
            self.money += bet
            print("You now have $", self.money, "\n")

        elif dealer_total < 21 and player_total > dealer_total:
            print("You win!")
            time.sleep(5)
            self.money += bet
            print("You now have $", self.money, "\n")

        elif dealer_total < 21 and player_total < dealer_total:
            print("You lose!")
            time.sleep(5)
            self.money -= bet
            print("You now have $", self.money, "\n")

        else:
            print("It's a tie! You get your money back!")
            time.sleep(5)
            print("You now have $", self.money, "\n")


player = Simulation()
player.play()