class TexasHoldemRules:
    """
    Standard Texas Hold'em hand rankings and casino rules.
    """

    def __init__(
        self,
        money,
        players=6,
        smallBlind=5,
        bigBlind=10,
        rakePercent=0.05,
        rakeCap=5.00
    ):
        self.money = money
        self.players = players
        self.smallBlind = smallBlind
        self.bigBlind = bigBlind
        self.rakePercent = rakePercent
        self.rakeCap = rakeCap

        self.cardRanks = [
            "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K", "A"
        ]

        self.cardSuits = [
            "Spades",
            "Hearts",
            "Diamonds",
            "Clubs"
        ]

        # Poker Hand Rankings (best to worst)
        self.handRankings = {
            "Royal Flush": 10,
            "Straight Flush": 9,
            "Four of a Kind": 8,
            "Full House": 7,
            "Flush": 6,
            "Straight": 5,
            "Three of a Kind": 4,
            "Two Pair": 3,
            "One Pair": 2,
            "High Card": 1
        }

        # Approximate probabilities of making each hand
        # by the river in Texas Hold'em
        self.handProbabilities = {
            "Royal Flush":      0.000032,
            "Straight Flush":   0.000279,
            "Four of a Kind":   0.00168,
            "Full House":       0.02596,
            "Flush":            0.03025,
            "Straight":         0.04619,
            "Three of a Kind":  0.04830,
            "Two Pair":         0.23496,
            "One Pair":         0.43824,
            "High Card":        0.17412
        }

    def getHandRank(self, handName):
        """Returns numeric strength of a hand."""
        return self.handRankings.get(handName, 0)

    def getHandProbability(self, handName):
        """Returns probability of making a hand by the river."""
        return self.handProbabilities.get(handName, 0.0)
