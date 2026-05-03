from slotRules import SlotsRules


class AutoSimulation(SlotsRules):
    """
    Plays slots autonomously using a flat bet strategy.
    """

    def __init__(self, starting_money=100, goal=200, bet=10):
        super().__init__(money=starting_money)
        self.starting_money = starting_money
        self.goal = goal
        self.bet = bet
        self.rounds_played = 0

    def play_round(self):
        _, net = self.play(self.bet)
        self.rounds_played += 1
        return "win" if net > 0 else "loss"

    def run(self):
        while self.bet <= self.money < self.goal:
            self.play_round()

        reached_goal = self.money >= self.goal
        return {
            "reached_goal": reached_goal,
            "final_balance": self.money,
            "rounds_played": self.rounds_played,
        }
