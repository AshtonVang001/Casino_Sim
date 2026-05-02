from blackJackRules import Rules


class AutoSimulation(Rules):
    """
    Plays blackjack autonomously using basic strategy:
    hit if hand total <= 16, stand at 17+.
    """

    def __init__(self, starting_money=100, goal=200, bet=10):
        super().__init__(money=starting_money)
        self.starting_money = starting_money
        self.goal = goal
        self.bet = bet
        self.hands_played = 0

    def _reset_deck(self):
        self.__init__(starting_money=self.money, goal=self.goal, bet=self.bet)

    def _refresh_deck(self):
        temp = Rules(money=self.money)
        self.deck = temp.deck

    def _player_strategy(self, hand):
        total = self.calculate_total(hand)
        return total < 17

    def play_hand(self):
        self._refresh_deck()

        player_hand = [self.draw_card(), self.draw_card()]
        dealer_hand = [self.draw_card(), self.draw_card()]

        player_total = self.calculate_total(player_hand)
        dealer_total = self.calculate_total(dealer_hand)

        self.hands_played += 1

        if player_total == 21:
            if dealer_total == 21:
                return "tie"
            self.money += self.bet * 1.5
            return "blackjack"

        while self._player_strategy(player_hand):
            player_hand.append(self.draw_card())
            player_total = self.calculate_total(player_hand)

            if player_total > 21:
                self.money -= self.bet
                return "bust"

        while dealer_total < 17:
            dealer_hand.append(self.draw_card())
            dealer_total = self.calculate_total(dealer_hand)

        if dealer_total > 21 or player_total > dealer_total:
            self.money += self.bet
            return "win"
        elif player_total < dealer_total:
            self.money -= self.bet
            return "loss"
        else:
            return "tie"

    def run(self):
        while self.bet <= self.money < self.goal:
            self.play_hand()

        reached_goal = self.money >= self.goal
        return {
            "reached_goal": reached_goal,
            "final_balance": self.money,
            "hands_played": self.hands_played,
        }
