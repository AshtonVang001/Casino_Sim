
class Rules:

    def __init__(self, money, cardNum = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"], cardSuits = ["Diamond", "Spade", "Hearts", "Clubs"], playerP = 0.42, dealerP = 0.49, pushP = 0.09):
        self.cardNum = cardNum
        self.cardSuits = cardSuits
        self.playerP = playerP
        self.dealerP = dealerP
        self.pushP = pushP
        self.money = money

