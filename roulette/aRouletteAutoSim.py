from aRoulette import A_Roulette, RED_NUMBERS, BLACK_NUMBERS


class AutoSimulation(A_Roulette):
    """
    Plays roulette autonomously using a flat red/black betting strategy.
    """

    def __init__(self, starting_money=100, goal=200, bet=10, strategy="red"):
        super().__init__(money=starting_money)
        self.starting_money = starting_money
        self.goal = goal
        self.bet = bet
        self.strategy = strategy
        self.rounds_played = 0

    def _get_bet_numbers(self):
        if self.strategy == "red":
            return list(RED_NUMBERS)
        elif self.strategy == "black":
            return list(BLACK_NUMBERS)
        # straight up on a specific number passed as strategy (e.g. strategy="17")
        return [int(self.strategy)]

    def play_round(self):
        bets = self._get_bet_numbers()
        net = self.resolve_bet(bets, self.bet)
        self.money += net
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
