import random

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}


class A_Roulette:
    # American Roulette: 0-36 plus 37 representing 00 (38 pockets total)

    def __init__(self, money=100):
        self.table_nums = list(range(0, 38))
        self.money = money

    def spin(self):
        return random.randrange(38)

    def resolve_bet(self, bets, bet_amount):
        """
        bets: list of pocket numbers to cover (0-37, where 37 = 00)
        Returns net gain/loss using standard inside-bet payout: (36 / len(bets)) - 1
        Works for outside even-money bets too (18 numbers -> 1:1 payout).
        """
        win_num = self.spin()
        if win_num in bets:
            return bet_amount * (36 / len(bets) - 1)
        return -bet_amount
