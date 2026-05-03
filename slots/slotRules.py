import random

class SlotsRules:
    """
    Simple 3-reel slot machine using standard casino-style payouts.
    """

    def __init__(
        self,
        money,
        symbols=None,
        jackpot=100,
        tripleP=0.02,
        doubleP=0.10
    ):
        self.money = money

        if symbols is None:
            self.symbols = [
                "Cherry",
                "Lemon",
                "Orange",
                "Plum",
                "Bell",
                "Bar",
                "Seven"
            ]
        else:
            self.symbols = symbols

        self.jackpot = jackpot
        self.tripleP = tripleP
        self.doubleP = doubleP

        # Standard payout table
        self.payouts = {
            "Seven": 50,
            "Bar": 25,
            "Bell": 15,
            "Cherry": 10
        }

    def spin(self):
        """Generate three random slot symbols."""
        return [random.choice(self.symbols) for _ in range(3)]

    def evaluate(self, reels, bet):
        """
        Calculate winnings based on reel outcome.
        Returns net profit.
        """
        # Three matching symbols
        if reels[0] == reels[1] == reels[2]:
            symbol = reels[0]
            multiplier = self.payouts.get(symbol, 5)
            return bet * multiplier

        # Two matching symbols
        if reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            return bet * 2

        # Special Cherry payout
        if reels.count("Cherry") == 1:
            return bet

        # Loss
        return -bet

    def play(self, bet):
        """
        Perform one slot machine spin.
        Returns (reels, winnings).
        """
        reels = self.spin()
        winnings = self.evaluate(reels, bet)
        self.money += winnings
        return reels, winnings
