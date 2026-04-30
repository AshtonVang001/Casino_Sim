import random as rand
#Class for a game of American Roulette
class A_Roulette():

    def __init__(self, bets = []):
        #37 represents 00
        self.tableNums = list(range[0, 37])

    #calculate the pocket the marble lands on
    def Marble(self):
        winNum = rand.randrange(37)
        return winNum
    
    def Play(self, bets, betAmount):
        win = Marble()
        #check to see if any bets hit, calculate and return money lost or gained
        for x in bets:
            if x == win:
                return (betAmount * (36/len(bets) - 1))
        return -betAmount